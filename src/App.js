//import logo from './logo.svg';
import './App.css';
import clayconn from './clayconn.svg'

export function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export function Navbar() {
  return (
    <div className="Navbar">
      <div>
        <a href='https://claytoncountyga.gov'>
          <img src={clayconn} alt='' />
        </a>
      </div>
      <div>
        <p>Clayton County Permitting</p>
      </div>
    </div>
  )
}

export default App;

//<img src={logo} className="App-logo" alt="logo" />
