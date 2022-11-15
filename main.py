import streamlit as st
import time

st.title('Streamlit 超入門')     


# st.write('DateFrame')

# df = pd.DataFrame({
#     '1列目': [1 , 2, 3, 4],
#     '2列目': [10 , 20, 30, 40]
# })

#st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
#writeを使用しない理由は形を変えられないから

#st.table(df.style.highlight_max(axis=0))

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.line_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2)/ [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

#コマンド/ 全行シャープ

st.write('プログレスバーの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせの回答')
# if st.checkbox('Show Image'):
#     img = Image.open('pct.png')
#     st.image(img, caption='youtube', use_column_width= True)

#  option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1, 11))
# )
# text = st.text_input(' あなたの趣味を教えてください。')
# condition = st.slider(' あなたの今の調子は？', 0, 100, 50)
# 'あなたの好きな数字は、', option, 'です。'
# 'あなたの趣味は: ', text
# 'コンディション: ', condition