from eval_nmt import load_pre_trained, evalText, viz_attn
from data_load import prepareData

eng2fra = True

if eng2fra:
    encoder_e2f, decoder_e2f, input_lang, output_lang, _ = load_pre_trained('eng-fra') 
    eng_text = 'i forgot to tell you about it .'
    inp1, out1, attn1 = evalText(eng_text, encoder_e2f, decoder_e2f, input_lang, output_lang)
    # viz_attn(inp1, out1, attn1)
             
# else:
    encoder_f2e, decoder_f2e, input_lang, output_lang, _ = load_pre_trained('fra-eng')
    fra_text = 'les amis sont faits pour ca .'
    inp2, out2, attn2 = evalText(fra_text, encoder_f2e, decoder_f2e, input_lang, output_lang)
    # viz_attn(inp2, out2, attn2)