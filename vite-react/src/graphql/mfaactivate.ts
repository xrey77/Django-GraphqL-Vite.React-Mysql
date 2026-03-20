import { gql } from '@apollo/client';

export const ACTIVATE_MFA = gql`
  mutation ActivateMfa($id: Int!, $twofactorenabled: Boolean!){
    activateMfa(id: $id, twofactorenabled: $twofactorenabled) {
      qrcodeurl
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

export interface MfaActivationData {
  activateMfa: UserData;
}

export interface MfaActivationVariables {
    id: number;
    twofactorenabled: boolean;
}
