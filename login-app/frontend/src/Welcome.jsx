import { useEffect, useState } from 'react'

export default function Welcome() {
    const [msg, setMsg] = useState('Loading...')
    const [error, setError] = useState('')

    useEffect(() => {
        fetch('/api/welcome', { credentials: 'include' })
            .then(async r => {
                if (!r.ok) {
                    const d = await r.json().catch(() => ({}))
                    throw new Error(d?.detail || 'Unauthorized')
                }
                return r.json()
            })
            .then(d => setMsg(d.message))
            .catch(err => setError(err.message))
    }, [])

    if (error) {
        return (
            <div style={{ fontFamily: 'sans-serif', maxWidth: 480, margin: '4rem auto' }}>
                <h2>Login required</h2>
                <p style={{ color: 'crimson' }}>{error}</p>
                <a href="/login">Go to Login</a>
            </div>
        )
    }

    return (
        <div style={{ fontFamily: 'sans-serif', maxWidth: 480, margin: '4rem auto' }}>
            <h2>{msg}</h2>
            <form method="post" onSubmit={async (e) => {
                e.preventDefault()
                await fetch('/api/logout', { method: 'POST', credentials: 'include' })
                window.location.href = '/login'
            }}>
                <button type="submit">Logout</button>
            </form>
        </div>
    )
}