# Construção de Analisadores Léxico e Sintático
## Trabalho II e III da Disciplina INE5421 - Linguagens Formais e Compiladores

1. Definição do Trabalho:

    O objetivo do trabalho é a construção de um analisador léxico (um autômato reconhecedor
    de itens léxicos) e de um analisador sintático (do tipo top down preditivo LL(1))
    para uma pseudolinguagem simples. Os analisadores léxico e sintático devem ser integrados
    de forma a permitir a validação sintática de pequenos programas fonte escritos na
    pseudolinguagem.

    A implementação do analisador léxico pode ser feita de forma “não automática” ou seja,
    dado um autômato resultante da união dos autômatos que representam os itens léxicos,
    este pode ser armazenado na memória ou implementado de forma implicita em rotinas e
    procedimentos.

    Para a construção do analisador sintático Preditivo LL(1) é necessário implementar o
    algoritmo para calcular os conjuntos FIRST e FOLLOW dos não terminais da GLC e
    automatizar a implementação da tabela de análise.
    A gramática Livre de contexto para a linguagem é apresentada abaixo (baseada no livro
    de Compiladores do Aho).

    ```
    < program > ::= < block >
    < block > ::= {< decls >< stmts >}
    < decls > ::= < decl >< decls > | ε
    < decl > ::= < type > id ;
    < type > ::= basic < types >
    < types > ::= [ num ] < types > | ε
    < stmts > ::= < stmt >< stmts > | ε
    < stmt > ::= < loc >=< bool > ;
                  | < matched_if >
                  | < open_if >
                  | while ( < bool > )stmt
                  | do < stmt > while ( < bool > );
                  | break ;
                  | < block >
    < matched_if > ::= if (< bool >)then < matched_if > else < matched_if >
    < open_if > ::= if (< bool >)then < stmt >
                    | if (< bool >)then < mached_if > else < open_if >
    < loc > ::= id < locs >
    < locs > ::= [ < bool > ] < locs > | ε
    < bool > ::= < join > | < join > || < bool >
    < join > ::= < equality > | < equality > && < join >
    < equality > ::= < rel > | < rel > == < equality > | < rel > ! = < equality >
    < rel > ::= < expr > < < expr > | < expr > <= < expr >
                | < expr > >= < expr > | < expr > > < expr > | < expr >
    < expr > ::= < term >< exprs >
    < exprs > ::= + < term >< exprs > | − < term >< exprs > | ε
    < term > ::= < unary >< terms >
    < terms > ::= ∗ < unary >< terms > | / < unary >< terms > | ε
    < unary > ::= ! < unary > | − < unary > | < f actor >
    < f actor > ::= (< bool >) | < loc > | num | real | true | false
    ```

    Os itens entre “< >” são categorias sintáticas (não terminais) os itens em negrito são terminais,
    assim como demais símbolos de separação e matemáticos. Para a construção do
    analisador léxico, devem ser observadas as construções possíveis na gramática, identificando
    palavras reservadas, caracteres especiais e identificadores.

2. Formato de Entrega: a parte do analisador léxico deve ser entregue via moodle até a data
de 22/11 as 14:00h. Sendo apresentado no dia 22/11. O trabalho II deve ser entregue via
moodle até dia 26/11 as 14:00h. Sendo apresentado nos dias 26/11 e 29/11. O trabalho
deve conter alguns programas fonte que sirvam para testar o compilador.

3. Grupos: Os grupos devem ser os mesmos do trabalho I.
