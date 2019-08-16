export type AccountType = 'CREATOR' | 'VIEWER';

export interface IUser {
    id: number;
    username: string;
    email: string;
    accountType: AccountType;
    dateJoined?: string;
    lastLogin?: string | null;
    latitude: number;
    longitude: number;
    searchDistance: number;
}
