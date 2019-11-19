import React from 'react';
import Register from './Register';
import Login from './Login';
import './App.css';
import HeaderComponent from './HeaderComponent';
// import DogContainer from './DogContainer';
import { Route, Switch } from 'react-router-dom';
const My404 = () => {
 return (
   <div>
     <h3>You are lost</h3>
   </div>
 )
}
function App() {
 return (
   <main>
     <HeaderComponent />
     <Switch>
       <Route exact path="/" component={ Register } />
       <Route exact path="/login" component={ Login } />
       {/* <Route exact path="/dogs" component={ DogContainer } /> */}
       <Route component={My404} />
     </Switch>
   </main>
 );
}
export default App;
