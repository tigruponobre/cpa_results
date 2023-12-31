--SUGESTIVAS PROFESSOR
SELECT DISTINCT
	C.NOME AS NOME,	
	CPA.resp_ra,
	REPLACE(REPLACE(CAST(CPA.resp_response AS NVARCHAR(MAX)),CHAR(13) + CHAR(10) ,' '), CHAR(10), '') AS SUGESTIVAS	
FROM OPENQUERY (
	HOSTGATOR, 
	'SELECT * FROM sur_response_teacher WHERE periodo_id = 15 AND resp_quest_id = 8 AND LENGTH(resp_response) >= 5' 
) CPA
INNER JOIN SMATRICULA MD ON(
	MD.RA = CAST(CPA.resp_ra AS VARCHAR)
)
INNER JOIN STURMADISC TD ON (	
	TD.CODCOLIGADA = MD.CODCOLIGADA
	AND TD.IDTURMADISC = MD.IDTURMADISC
	AND TD.IDPERLET = MD.IDPERLET
)
INNER JOIN SHABILITACAOFILIAL HF ON(
	HF.CODCOLIGADA = TD.CODCOLIGADA
	AND HF.IDHABILITACAOFILIAL = TD.IDHABILITACAOFILIAL
)
INNER JOIN SCURSO C ON(
	C.CODCOLIGADA = HF.CODCOLIGADA
	AND C.CODCURSO = HF.CODCURSO
)
WHERE MD.IDPERLET = 113
AND LEN(CAST(CPA.resp_response AS NVARCHAR)) >= 5
ORDER BY 
	C.NOME,
	CPA.resp_ra,
    SUGESTIVAS