import React from "react";
import Banner from "./Banner";
import CategoryCards from "./CategoryCards";
import Slider from "./Slider";
import "./home.css";
import axios from "axios";
import { useState, useEffect } from "react";
import ProductCard from "../ProductCard";
import "./Home.css";

export const Home = () => {
  const [recommendedProducts, setRecommendedProducts] = useState([]);

  useEffect(() => {
    fetchRecommendations();
    // console.log("reaching here");
  }, []); // This empty array ensures the effect runs only once on component mount

  const fetchRecommendations = async () => {
    try {
      const response = await axios.post("http://localhost:9000/recommend", {
        category: "All",
        user_id: localStorage.getItem("userId"), // Replace 'your_user_id_here' with the actual user ID
        n_recommendations: 5,
      });
      setRecommendedProducts(response.data.recommended_items);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  return (
    <div className="home">
      <Banner />
      <main>
        <div className="home-container">
          <h2>Featured Products</h2>
          <div className="product-grid">
            {recommendedProducts.map((product, index) => (
              <ProductCard key={product.item_id} product={product} />
            ))}
          </div>
        </div>
        <Slider
          title="Today's Deals"
          link_text="See all deals"
          arrFrom="0"
          arrTo="13"
          class="todaysDeals"
        />
        <Slider
          title="Up to 60% off on home products | Small businesses"
          link_text="See all offers"
          arrFrom="13"
          arrTo="22"
          class="SmallBusinesses"
        />
        <CategoryCards />
      </main>
      <div>
        {/* Render your recommended products here */}
        <ul>
          {recommendedProducts.map((product, index) => (
            <li key={product.item_id}>
              product:{product.item_id},similarity:
              {product.similarity.toFixed(2)}% manufacturer:{" "}
              {product.metadata?.results?.[0]?.content?.manufacturer ||
                "No Manufacturer"}{" "}
              - Price:{" "}
              {product.metadata?.results?.[0]?.content?.price || "No price"}{" "}
              rating:{" "}
              {product.metadata?.results?.[0]?.content?.rating || "No rating"}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Home;
