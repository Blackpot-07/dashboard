import streamlit as st

css_code = f"""
<style>
.appview-container .main .block-container {{
    margin-left : -20rem;
}}
</style>
"""
# st. set_page_config(layout="wide")
st.markdown(css_code, unsafe_allow_html=True)




# Your Streamlit app code
st.markdown("<h1 style='text-align: center;'>DashBoard</h1>", unsafe_allow_html=True)


st.markdown("<h3>Let us first explore the trends of volume and gross margin across different aspects </h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>OVERALL TRENDS</h1>", unsafe_allow_html=True)

with open("overall_gm_trend.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)

with open("overall_trend_volume.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)



st.markdown("<h1 style='text-align: center;'>TRENDS ACROSS BRANDS</h1>", unsafe_allow_html=True)

with open("gm_over_brands.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)


with open("vol_over_brands.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)



st.markdown("<h1 style='text-align: center;'>TRENDS ACROSS CUSTOMER TYPES</h1>", unsafe_allow_html=True)

with open("customertype_over_brands.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)


with open("customertype_vol_over_brands.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)


st.markdown("<h1 style='text-align: center;'> Distribution </h1>", unsafe_allow_html=True)
st.markdown("<h3>Moving on to the distribution of volume bought across customers </h3>", unsafe_allow_html=True)

with open("distribution_of_customer_vol_bought.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)


st.markdown("<h1 style='text-align: center;'> Contribution of each customer type </h1>", unsafe_allow_html=True)
st.markdown("<h3>contribution of the old, new and new retained customers in your total gross margin </h3>", unsafe_allow_html=True)

with open("pie_chart.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)

st.markdown("<h1 style='text-align: center;'> box and whiskers plot for customers </h1>", unsafe_allow_html=True)
st.markdown("<h3>the plot shows if any customer has given more than average gross margin to you guys, you can hover over the data points to check the customer id of that customer</h3>", unsafe_allow_html=True)

with open("box.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)

st.markdown("<h1 style='text-align: center;'> box and whiskers for skus </h1>", unsafe_allow_html=True)
st.markdown("<h3>the plot shows if any sku has given more than average gross margin to you guys, you can hover over the data points to check the customer id of that customer</h3>", unsafe_allow_html=True)

with open("box_sku.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)

st.markdown("<h1 style='text-align: center;'> REGIONAL PERFORMANCE </h1>", unsafe_allow_html=True)
st.markdown("<h3>Here we will show you the performance in terms of customers over different regions and also how much each brand has contributed in it</h3>", unsafe_allow_html=True)
st.markdown("<h3><br><br> Distribution of Customers in the top 10 regions</h3>", unsafe_allow_html=True)

with open("top_regions_customer_count.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)

st.markdown("<h3><br><br> Distribution of new Customers gained in the top 10 regions</h3>", unsafe_allow_html=True)
with open("top_regions_new_customercount.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)


st.markdown("<h2> IS THE DECLINE IN VOLUME DRIVEN BY LOSING CUSTOMERS? </h2>", unsafe_allow_html=True)
st.markdown("<h4> NO! by looking at the churn rate and the volume trend in the below graph, we can see that the customer volume trend shows a rather independent behavior with respect to churn except for in some cases which is quite random  </h4>", unsafe_allow_html=True)
with open("volume_and_churnrate_over_time.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)


st.markdown("<h1 style='text-align: center;'> HYPOTHESIS TESTING </h1>", unsafe_allow_html=True)
st.markdown("<h2> 1. Product Groups are not gaining new customers and existing business is slowly decreasing in sales </h2>", unsafe_allow_html=True)
st.markdown("<p> We can see that the number of new customers are increasing across time but the total gross margin is gradually decreasing which disproves this hypothesis <p>", unsafe_allow_html=True)
with open("newcustomer_vs_totalgrossmargint.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)


st.markdown("<h2> 2. Products are gaining new customers but losing customers of equal or greater size at the same rate </h2>", unsafe_allow_html=True)
st.markdown("<p>performing t-test suggests that there was a difference in the means of sales between new and old customers of same size but the graph below shows that the difference in the sales of existing and new customers is far to great for this hypothesis to be true<p>", unsafe_allow_html=True)
with open("h2_bar.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)

st.markdown("<h2>3. Products are not attractive to new business either through product offering or price-point </h2>", unsafe_allow_html=True)
st.markdown("<p> After applying muti Linear regression and observing the behavior of brands(product_offering) and price points to the volume bought, it was found that changing the price point does not affect the volume bought, but if the price point is kept the same, each brand causes a huge change in the sales, this shows that brands make a huge difference for customers to buy a product <p>", unsafe_allow_html=True)
with open("newcustomer_vs_totalgrossmargint.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)

st.markdown("<h2>4.Products are gaining new customers and we are holding onto these customers but new growth is being offset by decline in volume from our existing customers </h2>", unsafe_allow_html=True)
st.markdown("<p> t-test suggested that the difference between the volumes bought by old customer and new retained customers is pretty significant, upon visualizing we see that there is decline in the volume of old customers</p>", unsafe_allow_html=True)
with open("volumes_of_newretained_with_existing.html", "r",encoding='UTF-8') as file:
    plot_html = file.read()
st.components.v1.html(plot_html, width=1000, height=500)