import React from 'react'

import Accounts from './accounts'

import logo from './logo.svg'
import './App.css'

const App: React.FC = () => {
    const editText = 'Edit '
    const codeText = 'src/App.tsx'
    const saveText = ' and save to reload.'
    const header = (
        <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>
                {editText}
                <code>{codeText}</code>
                {saveText}
            </p>
            <a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
                Learn React
            </a>
        </header>
    )
    return (
        <div className="App">
            <Accounts />
        </div>
    )
}

export default App
