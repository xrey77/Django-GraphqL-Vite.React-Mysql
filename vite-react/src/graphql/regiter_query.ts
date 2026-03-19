import { gql } from '@apollo/client';



export const SIGNUP_MUTATION = gql`
  mutation RegisterUser(
    $firstName: String!, 
    $lastName: String!, 
    $email: String!, 
    $mobile: String!, 
    $username: String!, 
    $password: String!
  ) {
    userMutation(
      firstName: $firstName, 
      lastName: $lastName, 
      email: $email, 
      mobile: $mobile, 
      username: $username, 
      password: $password
    ) {
      message
      user {
        id
        username
        email
      }
    }
  }
  `
interface User {
  id: string;
  firstName: string;
  lastName: string;  
  email: string;
  mobile: string;
  username: string;
  password: string;
}

export interface CreateUserData {
  userMutation: User;
}

export interface CreateUserVariables {
    firstName: string;
    lastName: string;    
    email: string;
    mobile: string;
    username: string;
    password: string;
}
