import { gql } from '@apollo/client';

  // query ProductList($page: Int!) {
  //   productList(page: $page) {    
  //    page
  //    totpage
  //    totalrecords
  //    products {
  //      id
  //      category
  //      descriptions
  //      qty
  //      unit
  //      costprice
  //      sellprice
  //      saleprice
  //      productpicture
  //      alertstocks
  //      criticalstocks    
  //   }
  //  }
  // }

export const LIST_QUERY = gql`
  query pageProducts($page: Int!) {    
      pageProducts {
        productsList(page: $page) {
          page
          totpage
          totalrecords
          products {
            id
            category
            descriptions
            qty
            unit
            costprice
            sellprice
            saleprice
            productpicture
            alertstocks
            criticalstocks
          }
        }
    }
  }
`;



export interface ProductData {
    id: number
    category: string
    descriptions: string
    qty: number
    unit: string
    costprice: number
    sellprice: number
    saleprice: number
    productpicture: string
    alertstocks: number
    criticalstocks: number
}

export interface ProductListData {
  pageProducts: {
    productsList: {
      page: number;
      totpage: number;
      totalrecords: number;
      products: ProductData[];
    }
  };  
}

export interface ProductListVariables {
  page: number;
}


