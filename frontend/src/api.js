import axios from "axios"
import { ACCESS_TOKEN } from "./constants"

/**
 * Creates an Axios instance with the base URL set to the value of the `VITE_API_URL` environment variable.
 * This instance can be used to make API requests to the specified base URL.
 */
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN)
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }
)

export default api