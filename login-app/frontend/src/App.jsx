import { Routes, Route, Navigate } from 'react-router-dom'
import Login from './Login.jsx'
import Welcome from './Welcome.jsx'

export default function App() {
    return (
        <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/welcome" element={<Welcome />} />
            <Route path="*" element={<Navigate to="/login" replace />} />
        </Routes>
    )
}