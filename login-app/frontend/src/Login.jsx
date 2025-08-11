import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

export default function Login() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [error, setError] = useState('')
    const [loading, setLoading] = useState(false)
    const navigate = useNavigate()

    const submit = async (e) => {
        e.preventDefault()
        if (!username || !password) {
            setError('Username and password are required')
            return
        }
        setError('')
        setLoading(true)
        try {
            const res = await fetch('/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                credentials: 'include',
                body: JSON.stringify({ username, password })
            })
            if (!res.ok) {
                const data = await res.json().catch(() => ({}))
                throw new Error(data?.detail || 'Login failed')
            }
            navigate('/welcome', { replace: true })
        } catch (err) {
            setError(err.message)
        } finally {
            setLoading(false)
        }
    }

    return (
        <div style={{ maxWidth: 360, margin: '4rem auto', fontFamily: 'sans-serif' }}>
            <h1>Sign in</h1>
            {error && <div role="alert" style={{ color: 'crimson', marginBottom: 12 }}>{error}</div>}
            <form onSubmit={submit} noValidate>
                <div style={{ marginBottom: 12 }}>
                    <label>Username
                        <input name="username" value={username}
                            onChange={e => setUsername(e.target.value)} autoComplete="username" />
                    </label>
                </div>
                <div style={{ marginBottom: 12 }}>
                    <label>Password
                        <input type="password" name="password" value={password}
                            onChange={e => setPassword(e.target.value)} autoComplete="current-password" />
                    </label>
                </div>
                <button type="submit" disabled={loading}>{loading ? 'Signing in…' : 'Sign in'}</button>
            </form>
        </div>
    )
}