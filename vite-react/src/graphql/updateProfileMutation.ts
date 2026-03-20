import { gql } from '@apollo/client';

export const UPDATE_PROFILE = gql`
  mutation UpdateProfile(
  $id: Int!,
  $firstName: String!,
  $lastName: String!,
  $mobile: String!) {    
    updateMutation(
      id: $id,
      firstName: $firstName,
      lastName: $lastName,
      mobile: $mobile      
    ) {
    message
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
  userpic: string;
  qrcodeurl: string;
}

export interface ProfiledData {
  updateMutation: UserData;
}

export interface ProfileVariables {
    id: number;
    firstName: string
    lastName: string;
    mobile: string;
}
