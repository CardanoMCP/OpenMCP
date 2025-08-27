def test_prompts_exist():
    from src.server.ai.prompts import defi_analysis, contract_explanation, transaction_summary

    assert hasattr(defi_analysis, 'PROMPT')
    assert hasattr(contract_explanation, 'PROMPT')
    assert hasattr(transaction_summary, 'PROMPT') 