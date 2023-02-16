var connectionParams = {
  method: "GET",
  mode: "cors",
  headers: {
    "Access-Control-Allow-Origin": "*",
    Accept: "application/json",
    "Content-Type": "application/json",
  },
};
var limit = 15;

const searchQuerySort = (sort) => {
  let params = new URLSearchParams(window.location.search);
  let q = params.get("q");
  window.location.href =
    "./search-product-list.html?" +
    new URLSearchParams({ q: q, sort: sort.value, page: 1 });
};

window.onload = (() => {
  const queryString = location.search;
  const urlParams = new URLSearchParams(queryString);
  const page = parseInt(urlParams.get("page"));
  const offset = (page - 1) * limit;
  const sort = urlParams.get("sort");
  let q = urlParams.get("q");
  q = q == "" ? "*" : q;
  document.getElementById(
    "path"
  ).innerHTML += `<a href="./index.html" style="text-decoration:none;color:#bf616a" margin-left=20px>Home</a>/${
    q[0].toUpperCase() + q.slice(1)
  }`;
  document.getElementById("search-for").innerHTML = q;
  document.getElementById("product-query").innerHTML = q == "*" ? "all" : q;
  let searchParamsMap = { q: q };
  if (sort !== null && sort.length !== 0) {
    searchParamsMap["sort"] = sort;
  }
  fetch(
    "http://localhost:5000/search?" + new URLSearchParams(searchParamsMap),
    connectionParams
  )
    .then((response) => response.json())
    .then((data) => {
      const productsArr = data;
      let prodListDiv = document.getElementById("product-list-div");
      const newInnerHTML = productsArr
        .slice(offset, Math.min(offset + limit, productsArr.length))
        .map(
          (product) => `
          <div class="product-container" id="product-list-div" onclick = "window.open('Product.html?uniqueId=${product["id"]}','_blank');">
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
      const pages =
        Math.floor(productsArr.length / limit) +
        (productsArr.length % limit && 1);
      let paginationId = document.getElementById("pagination");
      if (page !== 1) {
        let searchParams = new URLSearchParams({
          ...searchParamsMap,
          page: page - 1,
        });
        paginationId.innerHTML += `<a href="./search-product-list.html?${searchParams}">&#10094;</a>`;
      }
      let paginationNewInnerHTMLArr = Array.from(
        { length: pages },
        (_, tempPage) => tempPage + 1
      ).map((tempPage) => {
        let searchParams = new URLSearchParams({
          ...searchParamsMap,
          page: tempPage,
        });
        return `<a href="./search-product-list.html?${searchParams}">${tempPage}</a>`;
      });
      let searchParams = new URLSearchParams({
        ...searchParamsMap,
        page: page,
      });
      paginationNewInnerHTMLArr[
        page - 1
      ] = `<a class="active" href="./search-product-list.html?${searchParams}">${page}</a>`;
      let paginationNewInnerHTML = paginationNewInnerHTMLArr.reduce(
        (x, y) => x + y
      );
      paginationId.innerHTML += paginationNewInnerHTML;
      if (page !== pages) {
        let searchParams = new URLSearchParams({
          ...searchParamsMap,
          page: page + 1,
        });
        paginationId.innerHTML += `<a href="./search-product-list.html?${searchParams}">&#10095;</a>`;
      }
    });
})();
