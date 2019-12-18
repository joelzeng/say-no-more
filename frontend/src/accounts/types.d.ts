export interface AccountData {
    accounts: Account[]
}

interface Account {
    name: string
    balance: number
    user: User
}

interface User {
    username: string
}
