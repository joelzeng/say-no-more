import gql from 'graphql-tag'

export const ACCOUNTS_QUERY = gql`
    {
        accounts {
            name
            balance
            user {
                username
            }
        }
    }
`
