const SearchBar = () => (
    <form action="/" method="get">
        <label htmlFor="header-search">
            <span className="visually-hidden">Lookup your address</span>
        </label>
        
        <input
            type="text"
            id="header-search"
            placeholder="Lookup your address"
            name="s" 
        />
        <button type="submit">Search</button>
    </form>
);

export default SearchBar;