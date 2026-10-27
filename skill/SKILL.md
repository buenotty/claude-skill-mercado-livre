---
name: mercado-livre-listing
description: Agente para lojistas de dropshipping no Mercado Livre. (1) Escolhe um produto do catálogo do fornecedor com margem líquida mínima e prepara o anúncio completo (título SEO, 7 imagens 1:1, descrição curta). (2) Avalia as promoções da Central de promoções do vendedor e diz quais compensam, comparando com o custo. Nunca publica nem aplica promoção sem o OK do dono da loja. Use quando pedirem "anúncio do dia", "novo produto no ML", "quais promoções aplicar".
---

# Mercado Livre: anúncio e promoções

Dois modos: `anúncio` (padrão) e `promoções`. Se o dono da loja não disser, faça promoções primeiro, depois o anúncio.

## Regras de ouro
- **Só margem.** Lucro líquido por venda de pelo menos 15% (ideal 20% ou mais) e, de preferência, acima de R$ 10.
- **Não mexa em anúncios existentes.** Só cria anúncio novo.
- **Nunca invente ficha técnica** (voltagem, material, pilha). Se um campo obrigatório não puder ser confirmado num anúncio idêntico de outro vendedor, descarte o produto.
- **Humano decide dinheiro.** Antes de publicar, mostre produto, preço e lucro em 5 linhas. Nunca clique em "Participar" de promoção sem o OK explícito: aplicar promoção muda preço.

## A conta
Preço mínimo para uma margem alvo, com a comissão da modalidade (hoje 11,5% no anúncio Clássico; confira) e o frete do "Resumo estimado das tarifas" do próprio formulário:

`preço mínimo = (custo + frete) / (1 - comissão - margem)`

O script `scripts/margin.py` faz essa conta e a conta inversa (lucro e margem de um preço dado).

## Anúncio do dia
1. **Dados.** Planilha de catálogo do fornecedor (SKU, nome, custo, peso, dimensões, EAN, NCM), estoque e lista dos SKUs que a loja já anuncia (não repetir).
2. **Filtro.** Custo e peso baixos (frete pesa), estoque alto, nada frágil, nada que exija ficha técnica que você não consiga confirmar. Calcule o preço mínimo para 20%.
3. **Mercado.** Busque o produto no Mercado Livre, veja preço e mais vendidos dos 12 primeiros, olhe os líderes. Exija preço de mercado maior ou igual ao preço mínimo.
4. **Ficha.** Descrição, fotos e vídeo no catálogo do fornecedor. Confirme voltagem, pilha e material num anúncio idêntico.
5. **Imagens (mínimo 7, todas 1:1, uma por vez).** 1 capa ambientada sem texto; 2 emoção com título de benefício; 3 cena de presente ou de uso; 4 infográfico com 4 destaques; 5 medidas; 6 funcionamento; 7 ambientes. Baixe logo após gerar e converta para JPG.
6. **Anúncio.** Título SEO de até 60 caracteres, marca e modelo, embalagem com as medidas do catálogo, fotos enviadas **uma por vez** na ordem final (envio em lote embaralha), estoque, EAN, SKU, descrição, modalidade e preço. Confira o "Resumo estimado das tarifas" antes de publicar.
7. **Descrição curta, no padrão dos líderes.** Abertura (o que é, marca, uso), benefício em duas frases, especificações (campo: valor), conteúdo da embalagem, observações (pilhas não inclusas, fotos ilustrativas). Sem perguntas e respostas, sem superlativo, sem material não confirmado.
8. **Promoção depois de publicar.** Sugira preço âncora ou cupom; o dono aplica.
9. **Fechar.** Registre produto, custo, preço, lucro e lições; liste o que não foi verificado.

## Gestão de promoções
1. Leia todas as páginas da Central de promoções e monte a tabela: SKU, preço atual, preço promocional, "Você recebe".
2. Cruze com o custo pelo SKU: lucro = "Você recebe" menos custo; margem = lucro dividido pelo preço promocional.
3. **Aplicar** só se lucro de pelo menos R$ 10 e margem de pelo menos 15%. Prejuízo vira **NÃO APLICAR**. SKU sem custo: "sem custo, não decidir". Margem boa com lucro abaixo de R$ 10: "fraco, só com o seu OK".
4. Se a proposta do Mercado Livre dá prejuízo, calcule o **maior desconto que ainda mantém 15%** e proponha esse valor, nunca o sugerido.
5. Cupom de seguidor e oferta relâmpago só em produto com margem de 25% ou mais.
6. Entregue a tabela ordenada (APLICAR, SÓ COM SEU OK, NÃO APLICAR) com o motivo em uma linha.

## Armadilhas
- A voltagem do formulário aceita texto livre; produto a pilha: "Pilhas".
- O frete real só aparece no resumo de tarifas. Item pesado ou volumoso vira prejuízo.
- Anúncios duplicados do mesmo SKU têm preços diferentes: avalie cada um.
- Reordenação da lista depois de aplicar: confira o status por ID de anúncio ao final.
