
# Parameters

    Name :                      maze_size_13_high_rest_chance-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     13
    Height :                    13
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      17783594736 function calls (17684077437 primitive calls) in 35608.74 seconds

##    Ordered by: cumulative time
   List reduced from 457 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35711.083 35711.083 {built-in method builtins.exec}
                      1    0.827    0.827 35711.083 35711.083 <string>:1(<module>)
                      1   80.241   80.241 35710.256 35710.256 main.py:10(teleport)
                3553296   13.329    0.000 10188.570    0.003 agent.py:26(learn)
                1776648  235.790    0.000 9618.896    0.005 collector.py:36(collect)
                8883240 8662.165    0.001 9359.548    0.001 {built-in method builtins.sum}
                3553296  264.609    0.000 8730.181    0.002 learner.py:42(Qlearn)
                1776648   62.739    0.000 6077.711    0.003 agent.py:50(_learn)
                1776648    7.056    0.000 5885.883    0.003 game.py:21(step)
                1776648    8.915    0.000 5511.238    0.003 layers.py:212(step)
        111908648/12434984  460.776    0.000 4184.096    0.000 module.py:866(_call_impl)
                1776648   54.615    0.000 4085.892    0.002 agent.py:101(_learn)
                1776649  158.278    0.000 4061.341    0.002 layers.py:192(update)
                8881688   26.067    0.000 3900.791    0.000 network.py:24(forward)
                8881688  121.610    0.000 3820.818    0.000 container.py:117(forward)
                3553296   31.107    0.000 3651.904    0.001 optimizer.py:84(wrapper)
                3553296   15.121    0.000 3505.260    0.001 grad_mode.py:24(decorate_context)
                3553296   97.702    0.000 3453.829    0.001 adam.py:55(step)
                1776648 1857.330    0.001 3376.636    0.002 replaybuffer.py:27(teleporter_save_data)
                3553296  712.842    0.000 3242.423    0.001 _functional.py:53(adam)
                1776648 1667.060    0.001 2950.222    0.002 agent.py:77(interveen)
                4444176   30.790    0.000 2873.755    0.001 layers.py:233(restart)
                3551744   87.159    0.000 2588.728    0.001 agent.py:45(__call__)
                4444176    5.848    0.000 2314.181    0.001 levels.py:8(__init__)
                4444176   14.705    0.000 2308.332    0.001 level.py:8(__init__)
                4444176  450.569    0.000 2254.711    0.001 levels.py:11(generate)
                3553296   15.193    0.000 2183.424    0.001 tensor.py:195(backward)
                3553296   13.944    0.000 2167.681    0.001 __init__.py:68(backward)
                3553296 2073.816    0.001 2073.816    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1776648  115.420    0.000 1429.571    0.001 layers.py:17(step)
               17763376   39.199    0.000 1401.088    0.000 conv.py:398(forward)
                1776648  855.309    0.000 1396.566    0.001 agent.py:59(modify)
               17763376   22.518    0.000 1344.976    0.000 conv.py:390(_conv_forward)
               17763376 1322.458    0.000 1322.458    0.000 {built-in method conv2d}
              177664800  148.514    0.000 1297.197    0.000 layer.py:66(move)
              101805791 1238.949    0.000 1238.949    0.000 {built-in method clone}
                1776648  592.818    0.000 1210.297    0.001 replaybuffer.py:23(sample_data)
                4444176  619.221    0.000 1205.708    0.000 levels.py:76(RFS)
               23091768   47.410    0.000 1092.283    0.000 linear.py:93(forward)
               23091768   19.772    0.000 1023.484    0.000 functional.py:1737(linear)
               23091768  998.017    0.000  998.017    0.000 {built-in method torch._C._nn.linear}
              177664800  104.274    0.000  848.448    0.000 layers.py:223(isFree)
                1776648   26.446    0.000  807.635    0.000 agent.py:96(__call__)
                5328392   34.900    0.000  780.888    0.000 agent.py:54(modify_board)
              409421116  679.826    0.000  744.174    0.000 layer.py:63(isFree)
               10660598   20.304    0.000  729.681    0.000 tensor.py:575(__iter__)
               10660598  690.170    0.000  690.170    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               63959328  652.083    0.000  652.083    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               14211632  632.308    0.000  632.308    0.000 {built-in method cat}
               31973456   26.304    0.000  612.563    0.000 activation.py:713(forward)
               63959328  592.224    0.000  592.224    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               31973456   27.915    0.000  586.260    0.000 functional.py:1364(leaky_relu)
               31973456  551.956    0.000  551.956    0.000 {built-in method torch._C._nn.leaky_relu}
                5329947  331.202    0.000  536.827    0.000 layer.py:90(update)
               13332528   44.655    0.000  523.364    0.000 layer.py:40(restart)
                3553296   84.234    0.000  521.085    0.000 optimizer.py:189(zero_grad)
                7531893  510.854    0.000  510.854    0.000 {built-in method tensor}
                5328392  500.618    0.000  500.618    0.000 {built-in method torch._C._nn.one_hot}
                1776648   32.173    0.000  498.793    0.000 replaybuffer.py:19(stacker)
              177664900   48.553    0.000  446.979    0.000 {built-in method builtins.all}
              536569129  119.145    0.000  417.629    0.000 layers.py:197(<genexpr>)
                3553296    4.194    0.000  390.430    0.000 game.py:17(board)
                4444276  200.244    0.000  366.428    0.000 layers.py:37(reset)
               31979664  361.357    0.000  361.357    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              107134183  336.223    0.000  336.223    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               31979664  313.773    0.000  313.773    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               31979664  303.452    0.000  303.452    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               31979664  296.901    0.000  296.901    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              622184640  193.109    0.000  291.594    0.000 levels.py:33(<genexpr>)
              177664900  187.463    0.000  284.497    0.000 layers.py:65(isDone)
                3551744   98.413    0.000  270.463    0.000 exploration.py:53(softmaxer)
              560300558  187.007    0.000  252.842    0.000 layer.py:76(add)
               31979664  235.710    0.000  235.710    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              223857702  154.441    0.000  192.309    0.000 tensor.py:906(grad)
              159990336   66.682    0.000  185.727    0.000 random.py:285(choice)
                3553296    4.956    0.000  174.733    0.000 loss.py:527(forward)
             1127110933  170.605    0.000  170.605    0.000 layer.py:85(elements)
                3553296   14.285    0.000  169.777    0.000 functional.py:2898(mse_loss)
              257881671  112.956    0.000  165.113    0.000 random.py:250(_randbelow_with_getrandbits)
              177664800  125.285    0.000  163.973    0.000 layers.py:229(check)
                6220824   57.917    0.000  149.124    0.000 random.py:315(sample)
              515422279   93.558    0.000  133.767    0.000 enum.py:646(__hash__)
              155546160  118.108    0.000  118.108    0.000 {method 'intersection_update' of 'set' objects}
             1791055607  115.793    0.000  115.793    0.000 {method 'append' of 'list' objects}
                3553296  111.259    0.000  111.259    0.000 {built-in method torch._C._nn.mse_loss}
        669079416/669079414   80.144    0.000  109.322    0.000 {built-in method builtins.len}
               17763376   12.584    0.000  105.360    0.000 flatten.py:39(forward)
              155546160  101.301    0.000  101.301    0.000 levels.py:86(<listcomp>)
                3553828   98.979    0.000   98.979    0.000 {built-in method max}
                5329944    7.678    0.000   97.613    0.000 tensor.py:525(__rsub__)
               17763376   92.776    0.000   92.776    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             1005072105   88.536    0.000   88.536    0.000 layer.py:59(positions)
                5329944   88.401    0.000   88.401    0.000 {built-in method rsub}
              122569246   87.229    0.000   87.229    0.000 {built-in method torch._C._get_tracing_state}
                3551744   86.982    0.000   86.982    0.000 {built-in method multinomial}
              875449260   86.791    0.000   86.791    0.000 {method 'add' of 'set' objects}
                1776648    6.756    0.000   82.788    0.000 exploration.py:47(epsilonGreedy)
              470212810   81.584    0.000   81.584    0.000 {built-in method builtins.min}
              226652976   80.652    0.000   80.652    0.000 level.py:25(inverse)
              472048610   79.676    0.000   79.676    0.000 {built-in method builtins.max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9393249: <maze_size_13_high_rest_chance_0> in cluster <dcc> Done

Job <maze_size_13_high_rest_chance_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 02:11:20 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 11:54:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 11:54:12 2021
Terminated at Mon Mar  8 21:49:45 2021
Results reported at Mon Mar  8 21:49:45 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35590.83 sec.
    Max Memory :                                 4893 MB
    Average Memory :                             3813.82 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               3299.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35734 sec.
    Turnaround time :                            70705 sec.

The output (if any) is above this job summary.

