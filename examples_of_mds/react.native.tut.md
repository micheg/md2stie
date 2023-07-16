---
title: Introduction to React Native
date: 2023-07-15
tags: React, HTML5, Reactive, functional, es6, native, android, IOS
summary: React Native is an open-source framework developed by Facebook that allows you to build mobile apps for iOS and Android using JavaScript and React.
slug: react_native
subtitle: Getting Started with React Native
---

# Getting Started with React Native

## Section 1: Introduction to React Native

1. What is React Native?
React Native is an open-source framework developed by Facebook that allows you to build mobile apps for iOS and Android using JavaScript and React. With React Native, you can create native mobile apps with a shared codebase, enabling faster development and access to native device features.

2. Advantages of React Native:
- **Cross-platform development**: React Native allows you to write a single source code for both iOS and Android.
- **Component-based**: React Native utilizes reusable components to build the user interface of your app.
- **Performance**: React Native apps use native components and are compiled into a native mobile app, providing performance similar to native apps.
- **Hot Reloading**: React Native supports hot reloading, allowing you to see code changes in real-time without having to fully reload the app.

## Section 2: Creating a New React Native Project

1. Creating a new React Native project:
Open your terminal and run the following command to create a new React Native project:

```
npx react-native init ProjectName
cd ProjectName
```

2. Running the app on an emulator/device:

- To run the app on an Android emulator:

```
npx react-native run-android
```

- To run the app on an iOS emulator:
```
npx react-native run-ios
```

1. Project structure:
The generated React Native project will have a basic structure that includes files such as `App.js` (the entry point of the app), `index.js` (app initialization), and an `android` folder (containing files specific to Android) and `ios` folder (containing files specific to iOS).

## Section 3: Components and User Interface

1. Creating a component:
In React Native, components are used to define the user interface of the app. Here's an example of creating a component:


```javascript
import React from 'react';
import { View, Text } from 'react-native';

const App = () => {
return (
    <View>
    <Text>Hello, world!</Text>
    </View>
);
};

export default App;
```

2. Using prebuilt components:
React Native provides a set of prebuilt components that can be used to create the app's user interface. For example, `View` is used as a container for elements, `Text` is used to display text, `Button` is used for buttons, and so on. You can import and use these components in your code.

3. Styles and layout:
React Native uses inline styles, similar to CSS, to apply styles to components. You can use the `StyleSheet` component to define styles and apply them to components. For example:


```javascript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const App = () => {
return (
    <View style={styles.container}>
    <Text style={styles.text}>Hello, world!</Text>
    </View>
);
};

const styles = StyleSheet.create({
container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
},
text: {
    fontSize: 20,
    fontWeight: 'bold',
},
});

export default App;
```

4. Handling events:
You can handle events for interactive elements using callback functions. For example, to handle a button click, you can use the `onPress` prop. Here's an example:

```javascript
import React from 'react';
import { View, Button, Alert } from 'react-native';

const App = () => {
const showAlert = () => {
    Alert.alert('You clicked the button!');
};

return (
    <View>
    <Button title="Click Me" onPress={showAlert} />
    </View>
);
};

export default App;
```

5. Custom components:
You can create and use your own custom components within your React Native app. Simply create a new file for the component and import it where needed. You can also pass data or functions as props to custom components.

## Section 4: Navigation

1. Installing a navigation library:
To enable navigation between different screens in your app, you can use a navigation library like `React Navigation`. You can install it in your React Native project by running the following command:

```
npm install @react-navigation/native
```

2. Configuring the navigation library:
Follow the installation and configuration instructions for `React Navigation` from their official documentation to set up the navigation library in your project. You'll also need to install a specific navigation navigator like `React Navigation Stack` or `React Navigation Bottom Tabs` based on your requirements.

3. Creating screens and routes:
In your project, create separate screens as React Native components for different sections of your app. Then, create routes using the navigation library to define the navigation between screens.

4. Example usage of React Navigation:
Here's an example of using `React Navigation` to create a basic stack-based navigation:

```javascript
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

const HomeScreen = () => (
<View>
    <Text>Home Screen</Text>
</View>
);

const DetailsScreen = () => (
<View>
    <Text>Details Screen</Text>
</View>
);

const App = () => (
<NavigationContainer>
    <Stack.Navigator>
    <Stack.Screen name="Home" component={HomeScreen} />
    <Stack.Screen name="Details" component={DetailsScreen} />
    </Stack.Navigator>
</NavigationContainer>
);

export default App;
```

In this example, we're creating two screens, `HomeScreen` and `DetailsScreen`. The screens are then registered in the navigation stack using `createStackNavigator`. Finally, the `NavigationContainer` component is used as the main container for the routes.


## Section 5: Accessing External Services

1. Making HTTP requests:
To make HTTP requests from a React Native app, you can use libraries like `axios` or the built-in `fetch` API. These libraries allow you to send HTTP requests to a server and handle the responses.

2. Example HTTP request using `axios`:
To use `axios`, you need to install it in your project by running the following command:

```
npm install axios
```

Here's an example of using `axios` to make a GET request:

```javascript
import React, { useEffect } from 'react';
import axios from 'axios';

const App = () => {
useEffect(() => {
    axios.get('https://api.example.com/data')
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.log(error);
    });
}, []);

return (
    <View>
    {/* User interface */}
    </View>
);
};

export default App;
```

In this example, we're making a GET request to the URL `'https://api.example.com/data'`. The response is handled inside the `useEffect` hook.

## Section 6: Testing and Deployment

1. Testing the app:
You can test your React Native app using testing frameworks like `Jest` and `React Testing Library`. These frameworks allow you to test components and app functionality to ensure everything works as expected.

2. App deployment:
To publish your React Native app to the respective platforms (iOS and Android), you'll need to follow the specific guidelines and processes for each platform. For iOS, you'll need an Apple Developer account and follow the App Store submission process. For Android, you'll need to generate an APK file or publish the app on the Google Play Store following the respective procedures.

This introductory tutorial provides an overview of the key concepts of React Native and helps you get started with building native mobile apps. Of course, there are many more aspects and features you can explore as you progress in app development.
