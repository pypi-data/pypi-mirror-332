"""
SHAP and ShapIQ based explainers for model interpretability.
"""
from typing import Any, Dict, List, Optional, Union, Tuple
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import shap
    SHAP_AVAILABLE = True
except ImportError:
    SHAP_AVAILABLE = False
    warnings.warn("shap package is not installed. ShapExplainer will not be available.")

try:
    import shapiq
    from shapiq.explainer import KernelExplainer as ShapIQKernelExplainer
    from shapiq.interactions import InteractionValues
    SHAPIQ_AVAILABLE = True
except ImportError:
    SHAPIQ_AVAILABLE = False
    warnings.warn("shapiq package is not installed. ShapIQExplainer will not be available.")


class ShapExplainer:
    """
    Wrapper for SHAP explainers to provide model interpretability.
    
    Parameters
    ----------
    model : Any
        The model to explain. Should have a `predict` method.
    model_type : str, default='tree'
        The type of model. Options: 'tree', 'linear', 'kernel'.
    """
    
    def __init__(self, model: Any, model_type: str = 'tree'):
        """Initialize the SHAP explainer."""
        if not SHAP_AVAILABLE:
            raise ImportError("shap package is required for ShapExplainer.")
        
        self.model = model
        self.model_type = model_type
        self.explainer = None
        self.is_fitted = False
        
        # Set a mapping of model_type to SHAP explainer
        self.explainer_mapping = {
            'tree': shap.TreeExplainer,
            'linear': shap.LinearExplainer,
            'kernel': shap.KernelExplainer,
        }
    
    def fit(self, X: Union[pd.DataFrame, np.ndarray]) -> 'ShapExplainer':
        """
        Fit the SHAP explainer to the data.
        
        Parameters
        ----------
        X : Union[pd.DataFrame, np.ndarray]
            The data to use for the explainer.
        
        Returns
        -------
        ShapExplainer
            The fitted explainer.
        """
        if self.model_type not in self.explainer_mapping:
            raise ValueError(f"Unknown model_type: {self.model_type}. "
                            f"Available options: {list(self.explainer_mapping.keys())}")
        
        # Convert pandas DataFrame to numpy array if necessary
        X_data = X
        if isinstance(X, pd.DataFrame):
            X_data = X.values
        
        # Create the explainer based on model_type
        if self.model_type == 'kernel':
            # Kernel explainer requires a function that returns numpy arrays
            def model_predict(X):
                return self.model.predict(X)
            self.explainer = self.explainer_mapping[self.model_type](model_predict, X_data)
        else:
            self.explainer = self.explainer_mapping[self.model_type](self.model, X_data)
        
        self.is_fitted = True
        return self
    
    def explain(self, X: Union[pd.DataFrame, np.ndarray]) -> Any:
        """
        Generate SHAP values to explain predictions.
        
        Parameters
        ----------
        X : Union[pd.DataFrame, np.ndarray]
            The data to explain predictions for.
        
        Returns
        -------
        Any
            SHAP values object.
        """
        if not self.is_fitted:
            raise ValueError("Explainer is not fitted. Call fit() first.")
        
        # Convert pandas DataFrame to numpy array if necessary
        X_data = X
        if isinstance(X, pd.DataFrame):
            X_data = X.values
        
        # Generate SHAP values
        shap_values = self.explainer.shap_values(X_data)
        
        # If the output is a list (for multi-class models), convert to a more usable format
        if isinstance(shap_values, list) and isinstance(X, pd.DataFrame):
            result = []
            for class_idx, class_shap_values in enumerate(shap_values):
                df = pd.DataFrame(class_shap_values, columns=X.columns, index=X.index)
                df['_class'] = class_idx
                result.append(df)
            return pd.concat(result)
        
        # For binary classification or regression with pandas input
        if isinstance(X, pd.DataFrame):
            return pd.DataFrame(shap_values, columns=X.columns, index=X.index)
        
        return shap_values
    
    def summary_plot(self, shap_values: Any, X: Union[pd.DataFrame, np.ndarray], **kwargs) -> None:
        """
        Generate a summary plot of SHAP values.
        
        Parameters
        ----------
        shap_values : Any
            SHAP values from the explain method.
        X : Union[pd.DataFrame, np.ndarray]
            The data used to generate the SHAP values.
        **kwargs : Dict
            Additional arguments to pass to shap.summary_plot.
        """
        if not SHAP_AVAILABLE:
            raise ImportError("shap package is required for summary_plot.")
        
        # Convert back to numpy if we converted to pandas in explain()
        if isinstance(shap_values, pd.DataFrame):
            class_values = shap_values['_class'].unique() if '_class' in shap_values.columns else [0]
            if '_class' in shap_values.columns:
                shap_values_list = []
                for class_idx in class_values:
                    class_df = shap_values[shap_values['_class'] == class_idx].drop('_class', axis=1)
                    shap_values_list.append(class_df.values)
                shap_values = shap_values_list
            else:
                shap_values = shap_values.values
        
        # Create the summary plot
        feature_names = X.columns.tolist() if isinstance(X, pd.DataFrame) else None
        shap.summary_plot(shap_values, X, feature_names=feature_names, **kwargs)


class ShapIQExplainer:
    """
    Wrapper for ShapIQ explainers to provide model interpretability with interactions.
    
    Parameters
    ----------
    model : Any
        The model to explain. Should have a `predict` method.
    max_order : int, default=2
        Maximum interaction order to compute. 1 = main effects, 2 = pairwise interactions, etc.
    """
    
    def __init__(self, model: Any, max_order: int = 2):
        """Initialize the ShapIQ explainer."""
        if not SHAPIQ_AVAILABLE:
            raise ImportError("shapiq package is required for ShapIQExplainer.")
        
        self.model = model
        self.max_order = max_order
        self.explainer = None
        self.interactions = None
        self.is_fitted = False
        self.feature_names = None
    
    def fit(self, X: pd.DataFrame, interaction_type: str = 'shapley_taylor') -> 'ShapIQExplainer':
        """
        Fit the ShapIQ explainer to the data.
        
        Parameters
        ----------
        X : pd.DataFrame
            The data to use for the explainer.
        interaction_type : str, default='shapley_taylor'
            The type of interaction values to compute.
            Options: 'shapley_taylor', 'faith_interactions', 'shapiq'
        
        Returns
        -------
        ShapIQExplainer
            The fitted explainer.
        """
        # Store feature names
        self.feature_names = X.columns.tolist()
        
        # Create a prediction function that returns numpy arrays
        def model_predict(X):
            return self.model.predict(X)
        
        # Create the ShapIQ explainer
        self.explainer = ShapIQKernelExplainer(model_predict, X.values)
        
        # Set the interaction type
        self.interaction_type = interaction_type
        
        self.is_fitted = True
        return self
    
    def explain(self, X: pd.DataFrame) -> Any:
        """
        Generate ShapIQ interaction values to explain predictions.
        
        Parameters
        ----------
        X : pd.DataFrame
            The data to explain predictions for.
        
        Returns
        -------
        Any
            ShapIQ interaction values object.
        """
        if not self.is_fitted:
            raise ValueError("Explainer is not fitted. Call fit() first.")
        
        # Generate interaction values based on the selected type
        if self.interaction_type == 'shapley_taylor':
            self.interactions = self.explainer.stx(X.values, max_order=self.max_order)
        elif self.interaction_type == 'faith_interactions':
            self.interactions = self.explainer.faith(X.values, max_order=self.max_order)
        elif self.interaction_type == 'shapiq':
            self.interactions = self.explainer.shapiq(X.values, max_order=self.max_order)
        else:
            raise ValueError(f"Unknown interaction_type: {self.interaction_type}. "
                           f"Available options: 'shapley_taylor', 'faith_interactions', 'shapiq'")
        
        return self.interactions
    
    def plot_main_effects(self, instance_idx: int = 0, top_k: int = 10, **kwargs) -> None:
        """
        Plot the main effects (first-order interactions) for a specific instance.
        
        Parameters
        ----------
        instance_idx : int, default=0
            The index of the instance to explain.
        top_k : int, default=10
            The number of top features to show.
        **kwargs : Dict
            Additional arguments to pass to the plotting function.
        """
        if self.interactions is None:
            raise ValueError("No interaction values available. Call explain() first.")
        
        # Extract main effects (order 1)
        main_effects = self.interactions.get_order(1)
        
        # Get values for the specified instance
        instance_values = main_effects.values[instance_idx]
        
        # Create a DataFrame with feature names
        effect_df = pd.DataFrame({
            'Feature': self.feature_names,
            'Effect': instance_values
        })
        
        # Sort by absolute value
        effect_df['Abs'] = effect_df['Effect'].abs()
        effect_df = effect_df.sort_values('Abs', ascending=False).head(top_k)
        
        # Plot
        plt.figure(figsize=(10, 6))
        plt.barh(effect_df['Feature'], effect_df['Effect'])
        plt.xlabel('SHAP Value')
        plt.title(f'Top {top_k} Main Effects for Instance {instance_idx}')
        plt.tight_layout()
        plt.show()
    
    def plot_interaction_effects(self, instance_idx: int = 0, top_k: int = 10, **kwargs) -> None:
        """
        Plot the pairwise interaction effects for a specific instance.
        
        Parameters
        ----------
        instance_idx : int, default=0
            The index of the instance to explain.
        top_k : int, default=10
            The number of top interactions to show.
        **kwargs : Dict
            Additional arguments to pass to the plotting function.
        """
        if self.interactions is None:
            raise ValueError("No interaction values available. Call explain() first.")
        
        if self.max_order < 2:
            raise ValueError("Pairwise interactions were not computed. Set max_order >= 2.")
        
        # Extract pairwise interactions (order 2)
        pairwise = self.interactions.get_order(2)
        
        # Get values for the specified instance
        instance_values = pairwise.values[instance_idx]
        
        # Create tuples of feature pairs
        pairs = []
        pair_values = []
        
        for i in range(len(self.feature_names)):
            for j in range(i+1, len(self.feature_names)):
                pair_name = f"{self.feature_names[i]} × {self.feature_names[j]}"
                pair_value = instance_values[i, j]
                pairs.append(pair_name)
                pair_values.append(pair_value)
        
        # Create a DataFrame
        interaction_df = pd.DataFrame({
            'Interaction': pairs,
            'Effect': pair_values
        })
        
        # Sort by absolute value
        interaction_df['Abs'] = interaction_df['Effect'].abs()
        interaction_df = interaction_df.sort_values('Abs', ascending=False).head(top_k)
        
        # Plot
        plt.figure(figsize=(12, 6))
        plt.barh(interaction_df['Interaction'], interaction_df['Effect'])
        plt.xlabel('Interaction Strength')
        plt.title(f'Top {top_k} Pairwise Interactions for Instance {instance_idx}')
        plt.tight_layout()
        plt.show()