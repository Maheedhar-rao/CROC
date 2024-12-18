import streamlit as st
import streamlit.components.v1 as components

# Set up the page
st.set_page_config(page_title="Pathway Catalyst", page_icon="🌐")

# Embed the HTML and CSS
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pathway Catalyst</title>
    <style>
        /* General Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'sans-serif';
            background-color: #f4f4f9;
            color: #333;
            padding: 20px;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
        }

        header img {
            width: 100px;
            height: auto;
            margin-bottom: 10px;
        }

        header h1 {
            font-size: 2.5rem;
            color: #4c8caf;
        }

        header p {
            font-size: 1.2rem;
            color: #555;
        }

        nav {
            display: flex;
            justify-content: center;
            background-color: #36bddb;
            padding: 10px 0;
            margin-bottom: 20px;
        }

        nav a {
            color: rgb(44, 37, 37);
            text-decoration: none;
            font-size: 1.67rem;
            margin: 0 15px;
            font-weight: bold;
        }

        nav a:hover {
            text-decoration: underline;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .filter-section {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .filter-section input {
            width: calc(100% - 20px);
            padding: 10px;
            font-size: 1rem;
            border: 1px solid #ddd;
            border-radius: 5px;
        }

        .table-wrapper {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }

        table th, table td {
            text-align: left;
            padding: 12px;
            border: 1px solid #ddd;
        }

        table th {
            background-color: #4CAF50;
            color: white;
        }

        table tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        footer {
            text-align: center;
            margin-top: 30px;
            font-size: 0.9rem;
            color: #777;
        }

        .button {
            display: inline-block;
            padding: 10px 15px;
            font-size: 1rem;
            color: white;
            background-color: #4CAF50;
            border: none;
            border-radius: 5px;
            text-decoration: none;
            text-align: center;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <header>
        <img src="logo.png" alt="Logo">
        <h1>Pathway Catalyst</h1>
        <p>See the Pathway, Be the Catalyst</p>
    </header>

    <nav>
        <a href="#">Home</a>
        <a href="#">Submissions</a>
        <a href="#">Approvals</a>
        <a href="#">Declines</a>
        <a href="#">Others</a>
    </nav>

    <div class="container">
        <div class="filter-section">
            <input type="text" id="filter" placeholder="Search by Name...">
            <a href="#" class="button">Apply Filter</a>
        </div>

        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Email</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>John Doe</td>
                        <td>johndoe@example.com</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>Jane Smith</td>
                        <td>janesmith@example.com</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <footer>
        &copy; 2024 Pathway Catalyst | Built with ❤️ for great UIs
    </footer>
</body>
</html>
"""

# Render the HTML
components.html(html_code, height=800)
