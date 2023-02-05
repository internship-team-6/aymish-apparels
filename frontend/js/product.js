window.onload = function () {
  let q = localStorage.getItem("query");
  var prod_div = document.getElementById("product-details");
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const product_id_search = urlParams.get("uid");
  const product_id_cat = urlParams.get("catuid");
  if (product_id_search != null) {
    fetch(`http://127.0.0.1:5000/product?uid=${product_id_search}`, {
      method: "GET",
      mode: "cors",
      headers: {
        "Access-Control-Allow-Origin": "*",
        Accept: "application/json",
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        try {
          console.log(data);
          //   var filtered_data = data[1][0];
          const products_arr = data;

          //   var tempid = String(filtered_data.uniqueId);
          var tempid = String(products_arr[0]);
          let title = products_arr[1];
          let img = products_arr[5];
          let price = products_arr[4];
          let desc = products_arr[3];
          console.log(tempid);
          prod_div.innerHTML += `<section id="product-details">
          <div class="image-slider">
          <img id="product_image" src="${img}" />
          </div>
          <div class="details">
            <p class="product-title">
              ${title}
            </p>
            <span class="product-price">$${price}</span>
            <p class="product-des">
              ${desc}
            </p>
          </div>
        </section>`;
        } catch (err) {
          console.log(err);
          // window.location = "404.html";
        }
        // document.getElementById("loader").style.display = "none";
      });
  }
};
