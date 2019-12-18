import React from 'react'
import { useQuery } from '@apollo/react-hooks'

import { ACCOUNTS_QUERY } from './queries'
import { AccountData } from './types.d'

export default function Accounts() {
    const { data, loading, error } = useQuery<AccountData>(ACCOUNTS_QUERY)
    if (loading) return <p>Loading..</p>
    if (error) return <p>ERROR</p>

    return (
        <div>
            {data &&
                data.accounts.map(account => (
                    <div>
                        {account.name}: ${account.balance} for
                        {account.user.username}
                    </div>
                ))}
        </div>
    )
}
