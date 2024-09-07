import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import '../styles/Form.css'
import LoadingIndicator from "./LoadingIndictor";

/**
 * Renders a form component that handles user authentication (login or registration).
 *
 * @param {Object} props - The component props.
 * @param {string} props.route - The API route for the authentication request.
 * @param {string} props.method - The authentication method, either "login" or "register".
 * @returns {JSX.Element} - The rendered form component.
 */
export default function Form({route, method}) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const name = method === "login" ? "Login" : "Register";

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault(); // Prevent the default form submission behavior, cancels refreshing the page

        try{
            const res = await api.post(route, {username, password});
            if (method  === "login") {
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                navigate("/");
            } else {
                navigate("/login");
            }
        }
        catch (error) {
            alert(error);
        } finally {
            setLoading(false);
        }
        
    }

    return <form  onSubmit={handleSubmit} className="form-container">
        <h1>{name}</h1>
        <input type="text" className="form-input" value={username}
            onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
        <input type="password" className="form-input" value={password}
            onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
        
        
        <button type="submit" className="form-button">{loading ? <LoadingIndicator /> : name}</button>
    </form>
}