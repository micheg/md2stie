---
title: Getting Started with React
date: 2023-07-14
tags: React, HTML5, Reactive, functional, es6
summary: React has revolutionized the way we build user interfaces for web applications. Developed by Facebook, React is a powerful JavaScript library that allows developers to create interactive and reusable UI components.
slug: react17
subtitle: Getting Started with React; Building Interactive User Interfaces
---


# Getting Started with React: Building Interactive User Interfaces

## Introduction

React has revolutionized the way we build user interfaces for web applications. Developed by Facebook, React is a powerful JavaScript library that allows developers to create interactive and reusable UI components. Whether you're new to web development or an experienced developer looking to learn React, this tutorial will guide you through the basics of setting up a React project and building your first interactive user interface.

## Prerequisites
Before diving into React, make sure you have a basic understanding of HTML, CSS, and JavaScript. Familiarity with ES6 syntax and concepts like functions, classes, and arrow functions will also be beneficial.

## Setting Up a React Project:

To get started with React, you'll need Node.js and npm (Node Package Manager) installed on your machine. Follow these steps to set up a new React project:

*Step 1:* Open your command line interface (CLI) and navigate to the desired directory where you want to create your project.

*Step 2:* Run the following command to create a new React project using the Create React App tool:

    ```bash
    npx create-react-app my-react-app
    ```

This command will create a new directory called "my-react-app" with the basic files and folder structure for a React project.

*Step 3:* Once the project is created, navigate to the project directory:

    ```bash
    cd my-react-app
    ```

*Step 4:* Start the development server by running the following command:

    ```bash
    npm start
    ```

This will launch the development server and open your React application in a web browser. You can now begin building your React components.

## Building Your First React Component:

React applications are built using reusable components. Components are JavaScript functions or classes that return a piece of UI. Let's create a simple "Hello World" component to get started:

*Step 1:* Open the `src/App.js` file in your code editor.

*Step 2:* Replace the existing code with the following:

    ```javascript
    import React from 'react';

    function App() {
    return (
        <div>
        <h1>Hello, React!</h1>
        </div>
    );
    }

    export default App;
    ```

This code defines a functional component named `App` that returns a `<div>` element containing an `<h1>` heading.

*Step 3:* Save the file and go back to your web browser. You should see the "Hello, React!" heading rendered on the screen.

Creating Reusable Components:
One of the key benefits of React is the ability to create reusable components. Let's create a custom component that can be reused in multiple places:

*Step 1:* Create a new file called `Greeting.js` in the `src` directory.

*Step 2:* Add the following code to the `Greeting.js` file:

    ```javascript
    import React from 'react';

    function Greeting(props) {
    return (
        <div>
        <h2>Welcome, {props.name}!</h2>
        </div>
    );
    }

    export default Greeting;
    ```

This code defines a functional component named `Greeting` that accepts a `name` prop and displays a personalized greeting.

*Step 3:* Open the `src/App.js` file again.

*Step 4:* Import the `Greeting` component by adding the following line at the top:

    ```javascript
    import Greeting from './Greeting';
    ```

*Step 5:* Replace the existing JSX code in the `App` component's return statement with the following:

    ```javascript
    return (
    <div>
        <h1>Hello, React!</h1>
        <Greeting name="John" />
        <Greeting name="Jane" />
    </div>
    );
    ```

This code uses the `Greeting` component twice, passing different names as props.

*Step 6:* Save the file and check your browser. You should now see the "Hello, React!" heading along with the personalized greetings rendered for "John" and "Jane".

## Conclusion

Congratulations! You've taken your first steps in learning React. In this tutorial, you set up a new React project, built a simple "Hello World" component, and created a reusable `Greeting` component. React's component-based architecture and reusability make it a powerful tool for building interactive user interfaces. As you delve deeper into React, you'll discover more advanced features and concepts that will help you create complex and dynamic web applications.
