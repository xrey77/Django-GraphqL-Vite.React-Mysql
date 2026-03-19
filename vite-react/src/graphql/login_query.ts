import { gql } from '@apollo/client';



export const SIGNIN_MUTATION = gql`
  mutation UserLogin($username: String!, $password: String!) {
    loginMutation(username: $username, password: $password) {
      user {
        id
        firstName
        lastName      
        email
        mobile
        username
        isActivated
        isBlocked
        userpicture
        mailtoken
        qrcodeurl
      }
      token
      message
    }
  }
  `
export interface User {
  id: string;
  firstName: string;
  lastName: string;  
  email: string;
  mobile: string;
  username: string;
  isactivated: number;
  isblocked: number;
  mailtoken: number;
  userpic: string;
  qrcodeurl: string;
}

export interface LoginUserData {
  loginMutation: User;
}

export interface LoginUserVariables {
    username: string;
    password: string;
}
