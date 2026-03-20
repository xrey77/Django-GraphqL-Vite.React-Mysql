import { gql } from '@apollo/client';

export const VERIFY_OTP = gql`
  mutation VerifyTotp($id: Int!, $otp: String!) {
    verifyTotp(id: $id, otp: $otp) {
      username
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

export interface OtpVerificationData {
  verifyTotp: UserData;
}

export interface OtpVerificationVariables {
    id: number;
    otp: string;
}
