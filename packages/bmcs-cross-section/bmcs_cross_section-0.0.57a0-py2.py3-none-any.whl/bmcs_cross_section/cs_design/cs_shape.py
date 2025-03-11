import traits.api as tr
from bmcs_utils.api import InteractiveModel
import numpy as np
import sympy as sp
from bmcs_utils.api import View, Item, Float, Array, Str, TextAreaEditor, Button, ButtonEditor
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
from matplotlib.patches import Circle as MPL_Circle
import shapely.geometry as sg

class ICrossSectionShape(tr.Interface):
    """This interface lists the functions need to be implemented by cross section classes."""

    def get_cs_area(self):
        """Returns the area of the cross section."""

    def get_cs_i(self):
        """Returns the moment of inertia of the cross section
         with respect to an axis passing through its centroid ."""

    def get_b(self, z_positions_array):
        """Returns b values that correspond to the positions z_positions_array."""


class CrossSectionShapeBase(InteractiveModel):
    """"This class describes the geometry of the cross section."""
    name = 'Cross Section Shape'

    H = Float(400, GEO=True)

    ipw_view = View(
        Item('H', minmax=(10, 3000), latex='H [mm]')
    )


@tr.provides(ICrossSectionShape)
class Rectangle(CrossSectionShapeBase):

    B = Float(200, GEO=True)

    ipw_view = View(
        *CrossSectionShapeBase.ipw_view.content,        # this will add View Items of the base class CrossSectionShapeBase
        Item('B', minmax=(10, 500), latex='B \mathrm{[mm]}')
    )

    def get_cs_area(self):
        return self.B * self.H

    def get_cs_i(self):
        return self.B * self.H ** 3 / 12

    def get_b(self, z_positions_array):
        return np.full_like(z_positions_array, self.B)

    def update_plot(self, ax):

        ax.fill([-self.B/2, self.B/2, self.B/2, -self.B/2, -self.B/2], [0, 0, self.H, self.H, 0], color='gray', alpha=0.2 )
        ax.plot([-self.B/2, self.B/2, self.B/2, -self.B/2, -self.B/2], [0, 0, self.H, self.H, 0], color='black')
        ax.autoscale_view()
        ax.set_aspect('equal')

        ax.annotate('Area = {} $mm^2$'.format(int(Rectangle.get_cs_area(self)), 0),
                    xy=(-self.H/2 * 0.8, self.H/2), color='blue')
        ax.annotate('I = {} $mm^4$'.format(int(Rectangle.get_cs_i(self)), 0),
                    xy=(-self.H/2 * 0.8, self.H/2 * 0.8), color='blue')


@tr.provides(ICrossSectionShape)
class Circle(CrossSectionShapeBase):

    H = Float(250, GEO=True)

    ipw_view = View(
        Item('H', minmax=(10, 3000), latex='D [mm]'),
    )

    def get_cs_area(self):
        return np.pi * self.H * self.H

    def get_cs_i(self):
        return np.pi * self.H ** 4 / 4

    def get_b(self, z_positions_array):
        return np.full_like(z_positions_array, self.H)

    def update_plot(self, ax):

        circle = MPL_Circle((0, self.H/2), self.H/2, facecolor=(.5,.5,.5,0.2), edgecolor=(0,0,0,1))

        ax.add_patch(circle)
        ax.autoscale_view()
        ax.set_aspect('equal')
        ax.annotate('Area = {} $mm^2$'.format(int(self.get_cs_area()), 0),
                    xy=(-self.H/2 * 0.8, self.H/2), color='blue')
        ax.annotate('I = {} $mm^4$'.format(int(self.get_cs_i()), 0),
                    xy=(-self.H/2 * 0.8, self.H/2 * 0.8), color='blue')


@tr.provides(ICrossSectionShape)
class TShape(CrossSectionShapeBase):

    B_f = Float(400, GEO=True)
    B_w = Float(100, GEO=True)
    H_w = Float(300, GEO=True)

    ipw_view = View(
        *CrossSectionShapeBase.ipw_view.content,
        Item('B_f', minmax=(10, 3000), latex=r'B_f \mathrm{[mm]}'),
        Item('B_w', minmax=(10, 3000), latex=r'B_w \mathrm{[mm]}'),
        Item('H_w', minmax=(10, 3000), latex=r'H_w \mathrm{[mm]}'),
    )

    def get_cs_area(self):
        return self.B_w * self.H_w + self.B_f * (self.H - self.H_w)

    def get_cs_i(self):
        A_f = self.B_f * (self.H - self.H_w)
        Y_f = (self.H - self.H_w) / 2 + self.H_w
        I_f = self.B_f * (self.H - self.H_w) ** 3 / 12
        A_w = self. B_w * self.H_w
        Y_w = self.H_w / 2
        I_w = self.B_w * self.H_w ** 3 /12
        Y_c = (Y_f * A_f + Y_w * A_w) / (A_f + A_w)
        I_c = I_f + A_f * (Y_c - Y_f)**2 + I_w + A_w * (Y_c - Y_w)**2
        return Y_c, I_c


    get_b = tr.Property(tr.Callable, depends_on='+input')

    @tr.cached_property
    def _get_get_b(self):
        z_ = sp.Symbol('z')
        b_p = sp.Piecewise(
            (self.B_w, z_ < self.H_w),
            (self.B_f, True)
        )
        return sp.lambdify(z_, b_p, 'numpy')

    def update_plot(self, ax):
        # Start drawing from bottom center of the cross section
        cs_points = np.array([[self.B_w / 2, 0],
                              [self.B_w / 2, self.H_w],
                              [self.B_f / 2, self.H_w],
                              [self.B_f / 2, self.H],
                              [-self.B_f / 2, self.H],
                              [-self.B_f / 2, self.H_w],
                              [-self.B_w / 2, self.H_w],
                              [-self.B_w / 2, 0]])

        cs = Polygon(cs_points)

        patch_collection = PatchCollection([cs], facecolor=(.5, .5, .5, 0.2), edgecolors=(0, 0, 0, 1))

        ax.add_collection(patch_collection)
        ax.scatter(0, TShape.get_cs_i(self)[0], color='white', s=self.B_w, marker="+")

        ax.autoscale_view()
        ax.set_aspect('equal')

        ax.annotate('Area = {} $mm^2$'.format(int(TShape.get_cs_area(self)), 0),
                    xy=(-self.H / 2 * 0.8, (self.H / 2 + self.H_w / 2)), color='blue')
        ax.annotate('I = {} $mm^4$'.format(int(TShape.get_cs_i(self)[1]), 0),
                    xy=(-self.H / 2 * 0.8, (self.H / 2 + self.H_w / 2) * 0.9), color='blue')
        ax.annotate('$Y_c$',
                    xy=(0, TShape.get_cs_i(self)[0] * 0.85), color='purple')

        # ax.annotate('$B_w$', xy=(-self.B_w / 2 , -self.B_w * 0.1), xytext=(self.B_w / 2 , -self.B_w * 0.1),
        #             arrowprops={'arrowstyle': '<->'}, va='center', ha ='center')
        # ax.annotate('$B_f$', xy=(-self.B_f / 2 , self.H * 1.1), xytext=(self.B_f / 2 , self.H * 1.1),
        #             arrowprops={'arrowstyle': '<->'}, va='center', ha ='center')
        # ax.annotate('$H$', xy=(-self.B_f / 2 , self.H * 1.1), xytext=(-self.B_f / 2 , self.H * 1.1 ),
        #             arrowprops={'arrowstyle': '<->'}, va='center', ha ='center')
        # ax.annotate('$H_w$', xy=(-self.B_f / 2 * 1.1, 0), xytext=(-self.B_f / 2 * 1.1 , self.H_w),
        #             arrowprops={'arrowstyle': '<->'}, va='center', ha ='center')


@tr.provides(ICrossSectionShape)
class IShape(CrossSectionShapeBase):

    H = Float(900, GEO=True)
    B_w = Float(50, GEO=True)
    B_f_bot = Float(200, GEO=True)
    B_f_top = Float(200, GEO=True)
    H_f_bot = Float(145, GEO=True)
    H_f_top = Float(145, GEO=True)

    ipw_view = View(
        *CrossSectionShapeBase.ipw_view.content,
        Item('B_w', minmax=(10, 3000), latex=r'B_w \mathrm{[mm]}'),
        Item('B_f_bot', minmax=(10, 3000), latex=r'B_{f_{bot}} \mathrm{[mm]}'),
        Item('B_f_top', minmax=(10, 3000), latex=r'B_{f_{top}} \mathrm{[mm]}'),
        Item('H_f_bot', minmax=(10, 3000), latex=r'H_{f_{bot}} \mathrm{[mm]}'),
        Item('H_f_top', minmax=(10, 3000), latex=r'H_{f_{top}} \mathrm{[mm]}'),
    )

    def get_cs_area(self):
        return self.B_f_bot * self.H_f_bot + self.B_f_top * self.H_f_top + self.B_w * (
                    self.H - self.H_f_top - self.H_f_bot)

    def get_cs_i(self):
        pass

    get_b = tr.Property(tr.Callable, depends_on='+input')

    @tr.cached_property
    def _get_get_b(self):
        z_ = sp.Symbol('z')
        b_p = sp.Piecewise(
            (self.B_f_bot, z_ < self.H_f_bot),
            (self.B_w, z_ < self.H - self.H_f_top),
            (self.B_f_top, True)
        )
        return sp.lambdify(z_, b_p, 'numpy')

    def update_plot(self, ax):
        # Start drawing from bottom center of the cross section
        cs_points = np.array([[self.B_f_bot/2, 0],
                              [self.B_f_bot / 2, self.H_f_bot],
                              [self.B_w / 2, self.H_f_bot],
                              [self.B_w / 2, self.H - self.H_f_top],
                              [self.B_f_top / 2, self.H - self.H_f_top],
                              [self.B_f_top / 2, self.H],
                              [-self.B_f_top / 2, self.H],
                              [-self.B_f_top / 2, self.H - self.H_f_top],
                              [-self.B_w / 2, self.H - self.H_f_top],
                              [-self.B_w / 2, self.H_f_bot],
                              [-self.B_f_bot / 2, self.H_f_bot],
                              [-self.B_f_bot / 2, 0]
                              ])

        cs = Polygon(cs_points)

        patch_collection = PatchCollection([cs], facecolor=(.5, .5, .5, 0.2), edgecolors=(0, 0, 0, 1))

        ax.add_collection(patch_collection)
        # ax.scatter(0, TShape.get_cs_i(self)[0], color='white', s=self.B_w, marker="+")

        ax.autoscale_view()
        ax.set_aspect('equal')

        ax.annotate('Area = {} $mm^2$'.format(int(IShape.get_cs_area(self)), 0),
                    xy=(0, self.H / 2), color='blue')


@tr.provides(ICrossSectionShape)
class CustomShape(CrossSectionShapeBase):

    H = tr.Property(GEO=True)
    def _get_H(self):
        pl = sg.Polygon(self.cs_points)
        top = pl.bounds[3]
        bot = pl.bounds[1]
        return top - bot

    cs_points_str = Str('60, 0\n60, 40\n25, 72.5\n25, 145\n200, 220\n200, 300\n-200, 300\n' +
                        '-200, 220\n-25, 145\n-25, 72.5\n-60, 40\n-60, 0')
    # apply_points_btn = Button()
    #
    # @tr.observe("apply_points_btn")
    # def apply_points_btn_clicked(self, event):
    #     print('This should update the plot with the new points, but maybe it\'s not needed')

    ipw_view = View(
        Item('cs_points_str', latex=r'\mathrm{Points}', editor=TextAreaEditor()),
        # Item('apply_points_btn', editor=ButtonEditor(label='Apply points', icon='refresh')),
    )

    _eps_tu = None
    eps_tu = tr.Property(desc='Ultimate concrete tensile strain', MAT=True)
    def _set_eps_tu(self, value):
        self._eps_tu = value
    def _get_eps_tu(self):
        if self._eps_tu is not None:
            return self._eps_tu
        else:
            return self.eps_cr

    _cs_points = None
    cs_points = tr.Property(GEO=True)
    def _get_cs_points(self):
        if self._cs_points is None:
            return self._parse_2d_points_str_into_array(self.cs_points_str)
        else:
            return self._cs_points
    def _set_cs_points(self, value):
        self._cs_points = value

    @staticmethod
    def _parse_2d_points_str_into_array(points_str):
        """ This will parse str of points written like this '0, 0\n 1, 1' to ([0, 0], [1, 1]) """
        points_str = points_str.replace('\n', ', ').replace('\r', ', ')
        points_array = np.fromstring(points_str, dtype=float, sep=',')
        if points_array.size % 2 != 0:
            points_array = np.append(points_array, 0)
        points_array = points_array.reshape((int(points_array.size / 2), 2))
        return points_array.reshape((int(points_array.size / 2), 2))

    def get_cs_area(self):
        points_xy = self.cs_points
        x = points_xy[:, 0]
        y = points_xy[:, 1]
        # See https://stackoverflow.com/a/30408825 for following Implementation of Shoelace formula
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    def get_cs_i(self):
        pass

    def get_b(self, z_positions_array):
        b = []
        # Make sure array is flat
        if isinstance(z_positions_array, np.ndarray):
            z_positions_array = z_positions_array.flatten()
        for z in z_positions_array:
            b.append(self._get_polygon_width_at_height(self.cs_points, z))
        return np.array(b)

    def _get_polygon_width_at_height(self, poly_points, height):
        p = sg.Polygon(poly_points)
        points = self._get_polygon_hor_line_intersection_points(p, height)
        minmax_diff = points[-1] - points[0]
        return minmax_diff

    def _get_polygon_hor_line_intersection_points(self, poly, y_val):
        """
        Find the intersection points of a horizontal line at
        y=`y_val` with the Polygon `poly`.
        Example:
        ---------
            import shapely.geometry as sg
            import matplotlib.pyplot as plt
            p = sg.Polygon(np.array([(0, 0),
                            (40, 30),
                            (10, 0)]))

            y_val = 10
            points = _get_polygon_hor_line_intersection_points(p, y_val)
            minmax = (points[0], points[-1])

            fig, ax = plt.subplots()
            ax.fill(*p.boundary.xy, color='y')
            ax.axhline(y_val, color='b')
            ax.plot(points, np.full_like(np.array(points), y_val) , 'b.')
            ax.plot(minmax, np.full_like(np.array(minmax), y_val) , 'ro', ms=10)
        """
        if y_val < poly.bounds[1] or y_val > poly.bounds[3]:
            raise ValueError('`y_val` is outside the limits of the Polygon.')
        if isinstance(poly, sg.Polygon):
            poly = poly.boundary
        hor_line = sg.LineString([[poly.bounds[0], y_val],
                                  [poly.bounds[2], y_val]])
        # print(poly.intersection(hor_line))
        intersec_elements = poly.intersection(hor_line)
        if isinstance(intersec_elements, sg.LineString):
            pts = [pt[0] for pt in intersec_elements.xy]
        else:
            pts = [pt.xy[0][0] for pt in intersec_elements.geoms]
        pts.sort()
        return pts

    def update_plot(self, ax):
        cs = Polygon(self.cs_points)
        patch_collection = PatchCollection([cs], facecolor=(.5, .5, .5, 0.2), edgecolors=(0, 0, 0, 1))
        ax.add_collection(patch_collection)
        # ax.scatter(0, CustomShape.get_cs_i(self)[0], color='white', s=self.B_w, marker="+")

        ax.autoscale_view()
        ax.set_aspect('equal')

        # ax.annotate('Area = {} $mm^2$'.format(int(CustomShape.get_cs_area(self)), 0),
        #             xy=(-self.H/2 * 0.8, self.H/2), color='blue')
        # ax.annotate('I = {} $mm^4$'.format(int(CustomShape.get_cs_i(self)), 0),
        #             xy=(-self.H/2 * 0.8, self.H/2 * 0.8), color='blue')