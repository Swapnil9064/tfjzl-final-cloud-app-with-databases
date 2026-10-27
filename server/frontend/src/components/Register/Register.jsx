import React, { useState } from "react";

export default function Register() {
  const [form, setForm] = useState({ username: "", firstName: "", lastName: "", email: "", password: "" });
  const [message, setMessage] = useState("");
  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = (e) => {
    e.preventDefault();
    setMessage("Registration form submitted. Connect this form to the backend registration endpoint to create an account.");
  };
  return <main className="container py-5" style={{ maxWidth: 560 }}>
    <div className="card border-0 shadow-sm"><div className="card-body p-4">
      <h1 className="h2 text-center">Sign Up</h1><p className="text-secondary text-center">Create your account</p>
      <form onSubmit={handleSubmit}>
        <div className="mb-3"><label className="form-label" htmlFor="username">Username</label><input className="form-control" id="username" name="username" value={form.username} onChange={handleChange} required /></div>
        <div className="mb-3"><label className="form-label" htmlFor="firstName">First Name</label><input className="form-control" id="firstName" name="firstName" value={form.firstName} onChange={handleChange} required /></div>
        <div className="mb-3"><label className="form-label" htmlFor="lastName">Last Name</label><input className="form-control" id="lastName" name="lastName" value={form.lastName} onChange={handleChange} required /></div>
        <div className="mb-3"><label className="form-label" htmlFor="email">Email</label><input className="form-control" type="email" id="email" name="email" value={form.email} onChange={handleChange} required /></div>
        <div className="mb-4"><label className="form-label" htmlFor="password">Password</label><input className="form-control" type="password" id="password" name="password" value={form.password} onChange={handleChange} minLength={8} required /></div>
        <button className="btn btn-primary w-100" type="submit">Register</button>
      </form>{message && <div className="alert alert-info mt-3" role="status">{message}</div>}
    </div></div>
  </main>;
}
