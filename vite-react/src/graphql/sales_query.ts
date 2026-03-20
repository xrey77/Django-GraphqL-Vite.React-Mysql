import { gql } from '@apollo/client';

export const SALES_QUERY = gql`
  query GetSales {
    getSales{
      salesList {
        salesamount
        salesdate
      }
    }
  }
`;


export interface SaleData {
    salesamount: number
    salesdate: string | number
}


export interface SalesListData {
  getSales: {
    salesList: SaleData[]
  }
}






