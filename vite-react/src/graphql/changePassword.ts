import { gql } from '@apollo/client';

export const CHANGE_PASSWORD = gql`
  mutation UpdatePassword(
    $id: Int!,
    $newPassword: String!) {
    updatePassword(
      id: $id,
      newPassword: $newPassword) {
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

export interface PasswordData {
  updatePassword: UserData;
}

export interface PasswordVariables {
    id: number;
    newPassword: string;
}
