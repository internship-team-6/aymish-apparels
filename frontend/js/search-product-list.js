// parameters to connect while using the fetch promise on any given url
var connectionParams = {
  method: "GET",
  mode: "cors",
  headers: {
    "Access-Control-Allow-Origin": "*",
    Accept: "application/json",
    "Content-Type": "application/json",
  },
};

// function to navigate to search-product-list page based on the provided sort order
const searchQuerySort = (sort) => {
  let params = new URLSearchParams(window.location.search);
  let q = params.get("q");
  window.location.href =
    "./search-product-list.html?" +
    new URLSearchParams({ q: q, sort: sort.value, page: 1 });
};

window.onload = (() => {
  const queryString = window.location.search;
  
  // obtain parameters
  const urlParams = new URLSearchParams(queryString);
  const page = parseInt(urlParams.get("page"));
  const sort = urlParams.get("sort");
  let q = urlParams.get("q");
  q = q == "" ? "*" : q;
  document.getElementById(
    "path"
  ).innerHTML += `<a href="./index.html" style="text-decoration:none;color:#bf616a" margin-left=20px>Home</a>/${
    q[0].toUpperCase() + q.slice(1)
  }`;
  document.getElementById("search-for").innerHTML = q;
  let modifiedQuery = q == "*" ? "all" : q;
  document.getElementById("product-query").innerHTML = modifiedQuery;
  document.title = "Search results for " + modifiedQuery;
  let searchParamsMap = { q: q, page: page };
  if (sort !== null && sort.length !== 0) {
    searchParamsMap["sort"] = sort;
  }
  // get list of products belonging to the given query along with total no. of pages
  fetch(
    "http://localhost:5000/search?" + new URLSearchParams(searchParamsMap),
    connectionParams
  )
    .then((response) => response.json())
    .then((data) => {
      const productsArr = data["product_list"];
      const pages = data["pages"];

      // update page with product details
      let prodListDiv = document.getElementById("product-list-div");
      const newInnerHTML = productsArr
        .map(
          (product) => `
            <div class="product-container" id="product-list-div" onclick = "window.open('product.html?uniqueId=${product["id"]}','_blank');">
              <div class="product-card">
                <div class="product-image">
                  <img src="${product["image"]}" class="product-thumb product-border" alt="" />
                </div>
                <div class="product-info">
                  <p class="product-title">${product["title"]}</p>
                  <span class="price">$${product["price"]}</span>
                </div>
              </div>
            </div>
            `
        )
        .reduce((x, y) => x + y);
      prodListDiv.innerHTML += newInnerHTML;

      // update page with pagination indicators
      let paginationId = document.getElementById("pagination");
      if (page !== 1) {
        paginationId.innerHTML += `<a href="./search-product-list.html?${new URLSearchParams(
          { ...searchParamsMap, page: page - 1 }
        )}">&#10094;</a>`;
        paginationId.innerHTML += `<a href="./search-product-list.html?${new URLSearchParams(
          { ...searchParamsMap, page: 1 }
        )}">1</a>`;
      }
      paginationId.innerHTML += `<a class="active" href="./search-product-list.html?${new URLSearchParams(
        { ...searchParamsMap, page: page }
      )}">${page}</a>`;
      if (page !== pages) {
        paginationId.innerHTML += `
          <a href="./search-product-list.html?${new URLSearchParams({
            ...searchParamsMap,
            page: pages,
          })}">${pages}</a>`;
        paginationId.innerHTML += `<a href="./search-product-list.html?${new URLSearchParams(
          {
            ...searchParamsMap,
            page: page + 1,
          }
        )}">&#10095;</a>`;
      }
    })
    .catch((err) => {
      window.location.href = "./404.html?";
    });
})();
