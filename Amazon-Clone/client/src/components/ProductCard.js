import React from "react";
import "./ProductCard.css";

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <img
        src={product.metadata?.results?.[0]?.content?.images?.[0]}
        alt={product.items_id}
        className="product-image"
      />
      <div className="product-details">
        <h3 className="product-name">
          {product.metadata?.results?.[0]?.content?.product_name}
        </h3>
        <p className="product-description">
          {product.metadata?.results?.[0]?.content?.brand}
        </p>
        <p className="product-description">
          {product.metadata?.results?.[0]?.content?.manufacturer}
        </p>
        <p className="product-description">
          {product.metadata?.results?.[0]?.content?.title}
        </p>
        <p className="product-description">
          {product.metadata?.results?.[0]?.content?.rating}
        </p>

        <p className="product-price">
          ${product.metadata?.results?.[0]?.content?.price}
        </p>
        <button className="product-btn">Add to Cart</button>
      </div>
    </div>
  );
}

export default ProductCard;
