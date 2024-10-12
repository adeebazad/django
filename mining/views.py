from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import MinedData
from .serializers import MinedDataSerializer
from django.http import JsonResponse
from sklearn.linear_model import LinearRegression
from datetime import timedelta
import pandas as pd 

class FetchOrderView (APIView):
    def get(self, request):
        # order = MinedData.objects.filter(is_used=False).first()
        order = MinedData.objects.all()
        if order:
            serializer = MinedDataSerializer(order, many=True)
            # order.is_used = False
            # order.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No unused orders available'},status=status.HTTP_404_NOT_FOUND)


class predict_order_prices(APIView) :

    def get(self,request):
        orders = MinedData.objects.all().values('order_date', 'order_total')
        df= pd.DataFrame(orders)

        df['order_date']= pd.to_datetime(df['order_date'].map(lambda date : date.toordinal()))
        x= df[['order_date']]
        y= df[['order_total']]

        model = LinearRegression()
        model.fit(x,y)

        future_dates = [(pd.Timestamp.now() + timedelta(days=i)).toordinal() for i in range (1,31)]
        predicted_prices =  model.predict([[date] for date in future_dates])

        future_dates_str = [(pd.Timestamp.now()+timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1,30)]
        predictions = list(zip(future_dates_str,predicted_prices))

        # print (predicted_prices)
        return Response({'predictions':predictions})