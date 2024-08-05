import { useState, useEffect } from "react";
import { ReleaseCardList } from "./ReleaseCardList";

import "../App.css";

function App() {
  const [error, setError] = useState(null);
  const [isLoaded, setIsLoaded] = useState(false);

  const [items, setItems] = useState([]);
  const [query, setQuery] = useState("");

  useEffect(() => {
    const params = new URLSearchParams({ search: query });
    let url = "http://localhost:8000/api/inventory/releases/";
    if (query.length > 0) {
      url = `http://localhost:8000/api/inventory/releases?${params.toString()}`;
    }
    fetch(url)
      .then((res) => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setItems(result.results);
        },
        (err) => {
          setIsLoaded(true);
          setError(err);
          console.error(error);
        }
      );
  }, [query, error]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(e.target.value);
  };

  return isLoaded ? (
    <div className="absolute top-0 z-[-2] h-screen w-screen bg-white bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.3),rgba(255,255,255,0))]">
      <div className="p-8 flex flex-row min-h-screen justify-center items-center">
        <p className="mb-6 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">
          This page is something to look at while I'm learning Rails.
          <br />
          No need to scroll down if you're sane.
        </p>
      </div>
      <div className="p-12">
        <div className="px-2">
          <input
            className="w-72 shadow appearance-none border rounded py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
            id="password"
            type="text"
            placeholder="Search..."
            onChange={handleInputChange}
            value={query}
          />
        </div>
        <ReleaseCardList releases={items} />
      </div>
    </div>
  ) : null;
}

export default App;
