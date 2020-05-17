import matplotlib.pyplot as plt


class MapSource:
    def __init__(self, dataset):
        self.df = dataset
        self.BBox = (self.df.Long.min(), self.df.Long.max(),
                     self.df.Lat.min(), self.df.Lat.max())
        self.columns = self.df.columns
        self.world_map = plt.imread('images/world-map-2.png')
        self.dates_list = self.df['Date'].unique()

    def date_world_map(self, date_num, status='Confirmed', color='b'):
        # display a map of a single day's infected, dead or recovered numbers
        date = self.dates_list[int(date_num)]

        fig, ax = plt.subplots(figsize=(8, 7))

        longs = self.df[self.df['Date'] == date]['Long']
        latis = self.df[self.df['Date'] == date]['Lat']

        size = self.df[self.df['Date'] == date][status].divide(100)

        ax.scatter(longs, latis, zorder=1, alpha=0.2, c=color, s=size)

        ax.set_title('Total Number of COVID-19 Reported Cases on: {}'.format(date))
        ax.set_xlim(self.BBox[0], self.BBox[1])
        ax.set_ylim(self.BBox[2], self.BBox[3])
        ax.imshow(self.world_map, zorder=0, extent=self.BBox, aspect='equal')
        # plt.show()

        return fig

