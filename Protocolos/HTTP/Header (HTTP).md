Access-Control-Allow-Origin

Permitir acesso de uma porta especifica:
`Access-Control-Allow-Origin: http://localhost:3000/`

É possível permitir o acesso de qualquer origem utilizando do símbolo **asterisco**, veja a seguir:

`Access-Control-Allow-Origin: *`

Isso não é uma medida recomendada pois permite que origens desconhecidas acessem o servidor, a não ser que seja intencional como no caso de uma API pública.