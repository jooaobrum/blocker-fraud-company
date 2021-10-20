mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"joaopaulo_brum@hotmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
" > ~/.streamlit/config.toml