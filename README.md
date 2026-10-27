# claude-skill-mercado-livre

Skill para o [Claude Code](https://claude.com/claude-code) que ajuda lojistas de dropshipping no Mercado Livre a:

1. **Escolher um produto e preparar o anúncio completo**: filtro por margem, checagem de mercado, 7 imagens 1:1, título SEO e descrição curta.
2. **Avaliar as promoções da Central de promoções**: cruza o que o Mercado Livre propõe com o seu custo e diz o que compensa, o que dá prejuízo e qual é o maior desconto que ainda mantém a margem.

*English: a Claude Code skill that picks a dropshipping product by margin, prepares a Mercado Livre listing, and reviews seller promotions against cost. It never publishes or joins a promotion without the owner's approval.*

## Princípios

- **Só margem.** Lucro líquido mínimo de 15% (ideal 20%).
- **Humano decide dinheiro.** O agente mostra produto, preço e lucro antes de publicar e nunca aplica uma promoção sem o OK explícito.
- **Nada inventado.** Ficha técnica que não puder ser confirmada num anúncio idêntico derruba o produto.

## A conta

```bash
python scripts/margin.py 20 10                 # preço mínimo para 20% de margem
python scripts/margin.py 20 10 --price 59.9    # lucro e margem de um preço
```

`preço mínimo = (custo + frete) / (1 - comissão - margem)`. A comissão padrão é a do anúncio Clássico no momento da escrita (11,5%); confira a taxa vigente. Os testes (`pytest`) cobrem a conta.

## Instalação

Copie a pasta `skill/` para `~/.claude/skills/mercado-livre-listing/` e peça ao Claude Code, por exemplo, "anúncio do dia" ou "quais promoções aplicar".

## Limites

- A skill conduz o navegador e depende de telas do Mercado Livre e do catálogo do fornecedor, que mudam. Ela **não** foi pensada para rodar sem supervisão.
- A conta de margem usa a comissão e o frete que você informa; não consulta a API do Mercado Livre.
- Esta é uma versão genérica: dados de loja, planilhas e regras específicas de uma operação ficam de fora.

## Sobre

Criada por Samuel Bueno, com IA sob supervisão. Licença MIT.
