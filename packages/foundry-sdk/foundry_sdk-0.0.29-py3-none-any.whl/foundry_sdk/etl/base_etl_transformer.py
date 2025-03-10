from abc import ABC, abstractmethod
import typing as t
import pandas as pd
from foundry_sdk.db_mgmt import SQLDatabase

import logging
logger = logging.getLogger(__name__)

class BaseETLTransformer(ABC):
    
    """Contains methods for extracting and transforming dataset information.

    See documentation how to get started with new test database:
    https://github.com/d3group/foundry-master/blob/main/documentation/new_db_set_up.md

    See documentation how to onboard a new dataset:
    https://github.com/d3group/foundry-master/blob/main/documentation/new_dataset_onboarding.md

    """

    def __init__(
        self,
        db: SQLDatabase,
        # all datasets indivially ...
    ):
        """Initialize the ETLTransformer object.

        Args:
            db (SQLDatabase): Database connection object.
            all datasets indivially ...
        """

        self.db = db
        # all datasets indivially ...

        self.clean_data()


    #################################### OPTIONAL: Data Cleaning ####################################
    
    def clean_data(self):
        """Clean the data by removing duplicates and missing values."""
        

        pass
    
#########################################################################################################
#################################### MANDATORY DATA EXTRACTION ##########################################
#########################################################################################################

    #################################### MANDATORY: Dates ###########################################

    @abstractmethod  
    def get_dates(self) -> t.Tuple[t.List, pd.Timestamp, pd.Timestamp]:
        """Generates all unique dates in the dataset along the min and max date.

        Returns:
            Dates: A Dates object created from the date column.
            min_date: The minimum date in the dataset.
            max_date: The maximum date in the dataset.
        """



       
        pass

 

    #################################### MANDATORY: Store-Region mapping ############################
    @abstractmethod
    def get_store_region_map(self) -> pd.DataFrame:
        
        """Convert a store region DataFrame into a mapping.
        
        Note: The dataframe must contain a columns "store" and "country". Then further levels (like "state") are optional.
        Country and states should follow ISO norms. Only one additional level can be added.
        If, e.g., a dataset is on city level, the only the city as lowest level should be added.

        Expecetd dataframe:
         - store: the name of the store (whatever raw identifier is in the dataset)
         - country: The country abbreviation according to ISO
        Optional:
         - [level_name]: the region abbreviation by level (level can be state, city, etc.)
        
        If there are no stores, then a dummy store must be used, country should be the country where
        most sales happen then.

        !Important!: The dummy store is DummyNames.DUMMY_STORE.value
        
        Returns:
            pd.DataFrame: Mapping of store names to region names.
        """


        pass



    #################################### MANDATORY: Categories ######################################

    @abstractmethod
    def get_category_level_description_map(self) -> pd.DataFrame:
        
        """Returns the description for each category level such as:
        
        {
            0: "name of highest level, e.g, "department"
            1: "name of second level, e.g., "category"
            2: "name of third level, e.g., "sub-category"
            3: ...
        }
        
        Note: This is mandatory, so e.g., if a dataset has only products flat, then one dummy 
        category must be create like:
        {0: "dummy_category_level"}

        !Important!: The dummy category lavel is DummyNames.DUMMY_CATEGORY_LEVEL.value

        Returns:
            dict: Mapping of category names and descriptions.
        """

        pass
    
    @abstractmethod
    def get_categories(self) -> pd.DataFrame:
        
        """

        This function sets the categorical hirarchy. The categories are spcified in a nested dictionary.

         - Each first-level key of the dectionary represents a level of a hirarchy (0 being highest level).
         - They values contain another dictionary with the following keys:
           - "category_name": The name of the category
           - "parent_category": A list of parent categories. If the category is on the highest level, the parent is None.
        

        The categories are expected to be in a dictionary with the following structure:
        {0:
            {
                "category_name": None
            }
        1:
            {
                "category_name": ["parent_category_1", "parent_category_2", ...]
            }
        ...
        }

        For the first level, the parent list should be None.

        If a category on a lower level has another parent from 2 or more levels above, the cateogry should be
        listed under the lowest level parent. (such that the write db function can first write all parents and then the children)
    
        !Important!: The dummy category is DummyNames.DUMMY_CATEGORY.value

        Returns:
            dict: A dictionary with the categories.
        
        """

        pass

    #################################### MANDATORY: Products ########################################
    
    @abstractmethod
    def get_products(self) -> pd.DataFrame:
        
        """Extract unique product names and associated last-level categories.

        Expected dataframe:
         - product: name/raw identifier of the product
         - category: The last level category that provides the link to the product

        Note 1: The products do not have to be unique (a product can belong to multiple categories).
        Note 2: If a dataset does not have products (e.g., aggregated store sales), a dummy product 
        must be used: dummy_product

        !Important!: The dummy product is DummyNames.DUMMY_PRODUCT.value
        !Important!: The dummy category is DummyNames.DUMMY_CATEGORY.value

        Returns:
            pd.DataFrame: DataFrame with product names and categories.
        """

        pass
    
    
    #################################### MANDATORY: Time-SKU data ###################################

    @abstractmethod
    def get_time_sku_data(self) -> pd.DataFrame:
        
        """Create a mapping of time-sku data.

        Expected dataframe:
         - date: date
         - product: name/raw identifier of the product
         - store: name/raw identifier of the store
         - sales: the sales demand for the product in the store on the date
        Optional: Further columns with time-sku data (e.g., price, promotion, etc.)

        !Important!: As a minimum this method must return the sales data.
        If a dataset does not have products (store-demands) or stores (just product-demands),
        then a dummy product or store name must be used (to be defined above in get_product_names
        or get_store_names).

        !Important!: The dummy product is DummyNames.DUMMY_PRODUCT.value
        !Important!: The dummy store is DummyNames.DUMMY_STORE.value

        Returns:
            pd.DataFrame: DataFrame with time-sku data.
        """

        pass
    

    #################################### MANDATORY: Not for sale and not available flag  ############
    
    @abstractmethod
    def get_not_for_sales_map(self) -> pd.DataFrame:

        """Generate a map of dates when a product was not sold in a given store.
        
        Expecetd dataframe:
         - date: date of the feature
         - store: the name of the store (whatever raw identifier is in the dataset)
         - product: name/raw identifier of the product
d
        There are no values, as the combination of data, store, and product shows
        that the product was not sold on that date in that store.

        !Important!: The dummy store is DummyNames.DUMMY_PRODUCT.value
        !Important!: The dummy product is DummyNames.DUMMY_PRODUCT.value

        Note: If every SKU in the dataset is always on sale, just return an empty dataframe.
        Yet, it is listed under mandatory bacause if there are cases in the data it must
        be implemented since it influences the training procedure.

        Returns:
            pd.DataFrame: DataFrame with dates when a product was not sold in a store
    
        """

        pass

    @abstractmethod
    def get_not_available_map(self) -> pd.DataFrame:

        """Generate a map of dates when a sales record is not available (missing value)
        
        Expecetd dataframe:
         - date: date of the feature
         - store: the name of the store (whatever raw identifier is in the dataset)
         - product: name/raw identifier of the product

        There are no values, as the combination of data, store, and product shows
        that the sales information is not available on that date in that store for that product.

        !Important!: The dummy store is DummyNames.DUMMY_PRODUCT.value
        !Important!: The dummy product is DummyNames.DUMMY_PRODUCT.value

        Note: If every SKU in the dataset has always as available values, just return an empty dataframe.
        Yet, it is listed under mandatory bacause if there are cases in the data it must
        be implemented since it influences the training procedure.

        Returns:
            pd.DataFrame: DataFrame with dates when a product was not sold in a store
    
        """

        pass
    
#########################################################################################################
#################################### OPTIONAL DATA EXTRACTION ###########################################
#########################################################################################################
    
    #################################### OPTIONAL: Store features ###################################
    
    @abstractmethod
    def get_store_feature_description_map(self) -> pd.DataFrame:
        
        """Returns the description for a store features.
        The name must match the name in get_store_feature_map

        Expecetd dataframe:
         - name: date of the feature
         - description: the name of the store (whatever raw identifier is in the dataset)

        If there are no store features, set an empty dictionary.

        Returns:
            pd.DataFrame
        """

        pass

    @abstractmethod
    def get_store_feature_map(self) -> pd.DataFrame:    
        
        """Creates a pandas DataFrame with all relevant store features.
        Store features are features that are store-specific but constant over time.

        Expecetd dataframe:
         - store: the name of the store (whatever raw identifier is in the dataset)
         - feature: the feature name
         - value: the value of the feature

        There can be multiple store features (e.g., store_category, store_size)

        If there are no store specific features, return an empty dataframe

        Returns:
            pd.DataFrame: Dictionary with time-region feature values.
       
        """

        pass
    

    #################################### OPTIONAL: Time-Product features ############################
    
    @abstractmethod
    def get_time_product_feature_description_map(self) -> pd.DataFrame:
        
        """Returns the description for a store features.
        The name must match the name in get_store_feature_map

        Expecetd dataframe:
         - name: date of the feature
         - description: the name of the store (whatever raw identifier is in the dataset)

        If there are no store features, set an empty dictionary abote to return an 
        empty dataframe.

        Returns:
            pd.DataFrame
        """

        pass

    @abstractmethod
    def get_time_product_feature_map(self) -> pd.DataFrame:    
        
        """Creates a pandas DataFrame with all relevant time-product features.
        Time product features are features that are product-specific but independent
        of stores (like online product ratings) and vary over time.

        Expecetd dataframe:
         - date: date of the feature
         - product: name/raw identifier of the product
         - feature: the feature name
         - value: the value of the feature

        There can be multiple time-product features (e.g., product_rating, number_of_reviews)

        If there are no time-product specific features, return an empty dataframe

        Returns:
            pd.DataFrame: Dictionary with time-product feature values.
       
        """

        pass


    #################################### OPTIONAL: Time-Region features #############################
    
    @abstractmethod 
    def get_time_region_feature_description_map(self) -> pd.DataFrame:
        
        """Returns the description for a time-region feature.
        The name must match the name in get_time_region_feature_map

        Expecetd dataframe:
         - name: date of the feature
         - description: the name of the store (whatever raw identifier is in the dataset)

        Returns:
            pd.DataFrame: Dictionary with time-region feature values.
        """

        pass

    @abstractmethod
    def get_time_region_feature_map(self) -> pd.DataFrame:    
        
        """Creates a pandas DataFrame with all relevant time-region features.
        Time region features are features that vary over time and by region.

        Expected dataframe:
         - date: date of the feature
         - country: country abbreviation according to ISO
         - feature: the feature name
         - value: the value of the feature
         Optional:
         - [level_name]: the lowest level region in the dataset that maps to the stores if this is not country.The columnn name should be the appropriate level such as "state" or "city"

        There can be multiple time-region features (e.g., weather, holidays)

        If there are no time-region specific features, return an empty dataframe

        Returns:
            pd.DataFrame: Time region feature values. 
       
        """

        pass

    #################################### OPTIONAL: Time-Store features ##############################

    @abstractmethod
    def get_time_store_feature_description_map(self) -> pd.DataFrame:
        
        """
        Returns the description for a time-store feature.
        The name must match the name in get_time_store_feature_map.

        Expected DataFrame:
        - name: the feature name
        - description: a description of the feature

        Returns:
            pd.DataFrame: DataFrame with time-store feature values.
        """

        pass

    @abstractmethod
    def get_time_store_feature_map(self) -> pd.DataFrame:
        
        """Creates a pandas DataFrame with all relevant time-store features.
        Time store features are features that vary over time and by store.

        Expecetd dataframe:
         - date: date of the feature
         - store: the name of the store (whatever raw identifier is in the dataset)
         - feature: the feature name
         - value: the value of the feature

        There can be multiple time-store features (e.g., weather, holidays)

        If there are no time-store specific features, return an empty dataframe

        Returns:
            pd.DataFrame: Dictionary with time-store feature values.
       
        """

        pass