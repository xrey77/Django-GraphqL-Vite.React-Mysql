import { gql } from '@apollo/client';

export const GETUSERID_QUERY = gql`
  query GetUserId($id: Int!) {
    getuserId {
      user(id: $id) {
        id
        firstName
        lastName
        email
        mobile
        username
        isActivated
        isBlocked
        mailtoken
        userpicture
        qrcodeurl    
      }
    }
  }
`;

export interface UserData {
  id: number;
  firstName: string;
  lastName: string;
  email: string;
  mobile: string;
  username: string;
  isActivated: boolean;
  isBlocked: boolean;
  mailtoken: string;
  userpicture: string;
  qrcodeurl?: string;
}

export interface GetUserIdData {
  getuserId: {
    user: UserData;    
  }
}

export interface GetUserIdVariables {
  id: number;
}
