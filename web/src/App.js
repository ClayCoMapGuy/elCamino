//import logo from './logo.svg';
import './App.css';
import { Cards } from './Navigation/QuestionCards'
import Search from './Navigation/Searchbar'

export function App() {
  return (
    <div className="App">
      <Search />
      <Cards />
    </div>
  );
}
