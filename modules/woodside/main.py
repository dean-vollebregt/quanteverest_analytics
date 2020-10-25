from functions.get_data import brent_crude
from functions.prepare_data import prepare_brent, prepare_woodside
from functions.LTSM_model import LTSM_model
from functions.graph_forecast import graph_forecast
from services.s3_service import upload_image

def main():
    brent_crude()
    brent_data = prepare_brent()
    woodside_data = prepare_woodside()
    woodside_forecast = LTSM_model(brent_data, woodside_data)
    woodside_graph = graph_forecast(woodside_data, woodside_forecast)
    upload_image()

main()