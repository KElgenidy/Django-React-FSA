import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./components/Login";
import Register from "./components/Register";
import Home from "./components/Home";
import NotFound from "./components/NotFound";

import ProtectedRoute from "./components/ProtectedRoute";

/**
 * Clears the user's localStorage and navigates them to the login page.
 * This function is used to log the user out of the application.
 */
function Logout() {
  localStorage.clear();
  return <Navigate to="/login" />;
}

/**
 * Clears the user's localStorage and navigates them to the login page.
 * This function is used to log the user out of the application.
 */
function RegisterAndLogout() {
  localStorage.clear();
  return <Register />;
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />

        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="/*" element={<NotFound />} />
        <Route path="/logout" element={<Logout />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
