// Home.js
import React from "react";
import ProductCard from "../components/ProductCard";
import "./Home.css";

function Cellphones() {
  //Added Data
  const [recommendedProducts, setRecommendedProducts] = useState([]);

  useEffect(() => {
    fetchRecommendations();
    // console.log("reaching here");
  }, []); // This empty array ensures the effect runs only once on component mount

  const fetchRecommendations = async () => {
    try {
      const response = await axios.post("http://localhost:9000/recommend", {
        category: "Cell_Phones_and_Accessories",
        user_id: localStorage.getItem("userId"), // Replace 'your_user_id_here' with the actual user ID
        n_recommendations: 10,
      });
      setRecommendedProducts(response.data.recommended_items);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  return (
    <div className="home-container">
      <h2>Featured Products</h2>
      <div className="product-grid">
        {products.map((product) => (
          <ProductCard key={product.item_id} product={product} />
        ))}
      </div>
    </div>
  );
}

export default Cellphones;
