
# Parameters

    Name :                      Causal3_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      57750940200 function calls (57404025165 primitive calls) in 86123.20 seconds

##    Ordered by: cumulative time
   List reduced from 510 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86123.204 86123.204 {built-in method builtins.exec}
                      1    3.883    3.883 86123.204 86123.204 <string>:1(<module>)
                      1  273.743  273.743 86119.321 86119.321 main.py:80(CFagent)
                8152755   29.758    0.000 24510.521    0.003 agent.py:29(learn)
                2717585 2457.721    0.001 22471.892    0.008 agent.py:212(counterfact)
                8152755  606.265    0.000 20545.021    0.003 learner.py:42(Qlearn)
        384881406/37968062 1551.257    0.000 13814.499    0.000 module.py:866(_call_impl)
                2717585   12.598    0.000 13401.115    0.005 game.py:42(step)
               29815307   84.380    0.000 13099.185    0.000 network.py:28(forward)
               29815307  406.427    0.000 12829.231    0.000 container.py:117(forward)
                2717585   16.839    0.000 12789.017    0.005 layers.py:827(step)
                2717585  261.276    0.000 9437.069    0.003 agent.py:54(_learn)
                2717585  259.365    0.000 8752.569    0.003 agent.py:204(_learn)
                8152755   70.259    0.000 8702.094    0.001 optimizer.py:84(wrapper)
               93580475 8670.460    0.000 8670.460    0.000 {built-in method tensor}
               87267230   53.623    0.000 8521.726    0.000 game.py:38(board)
                8152755   33.446    0.000 8370.435    0.001 grad_mode.py:24(decorate_context)
                8152755  237.187    0.000 8256.673    0.001 adam.py:55(step)
                5397001  111.864    0.000 8222.810    0.002 agent.py:176(choose_action)
                2717585  225.613    0.000 7800.632    0.003 layers.py:17(step)
                8152755 1675.599    0.000 7753.924    0.001 _functional.py:53(adam)
               10830381  253.255    0.000 7627.467    0.001 agent.py:49(__call__)
              271331627  426.431    0.000 7552.533    0.000 layer.py:106(move)
                2717585   74.358    0.000 6274.275    0.002 agent.py:117(_learn)
                2717585 3099.351    0.001 5769.632    0.002 replaybuffer.py:28(teleporter_save_data)
                8152755   42.903    0.000 5242.707    0.001 tensor.py:195(backward)
                8152755   32.031    0.000 5198.498    0.001 __init__.py:68(backward)
                8152755 4983.923    0.001 4983.923    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2717586  384.377    0.000 4950.253    0.002 layers.py:793(update)
                2717585 2897.310    0.001 4817.080    0.002 agent.py:88(interveen)
               59630614  126.972    0.000 4561.118    0.000 conv.py:398(forward)
                2717585 3619.169    0.001 4475.401    0.002 replaybuffer.py:22(sample_data)
               86962712 2360.236    0.000 4417.051    0.000 layer.py:175(NoRock_update)
              271331627  927.900    0.000 4395.584    0.000 layers.py:844(check)
               59630614   78.384    0.000 4378.277    0.000 conv.py:390(_conv_forward)
                2717585 3513.003    0.001 4352.742    0.002 replaybuffer.py:67(sample_data)
               59630614 4299.893    0.000 4299.893    0.000 {built-in method conv2d}
               84010751  166.550    0.000 3738.887    0.000 linear.py:93(forward)
               84010751   65.698    0.000 3495.540    0.000 functional.py:1737(linear)
               84010751 3412.425    0.000 3412.425    0.000 {built-in method torch._C._nn.linear}
              195074985 2473.028    0.000 2473.028    0.000 {built-in method clone}
                2717585 1594.722    0.001 2379.960    0.001 agent.py:67(modify)
              271331627  414.813    0.000 2329.208    0.000 layers.py:838(isFree)
              113826058   87.829    0.000 2069.021    0.000 activation.py:713(forward)
              113826058   89.715    0.000 1981.192    0.000 functional.py:1364(leaky_relu)
               13547966   89.487    0.000 1930.490    0.000 agent.py:59(modify_board)
             1908575128 1594.777    0.000 1914.395    0.000 layer.py:103(isFree)
              113826058 1871.289    0.000 1871.289    0.000 {built-in method torch._C._nn.leaky_relu}
                5397001 1476.142    0.000 1726.544    0.000 agent.py:187(convert_values)
               40723816 1611.982    0.000 1611.982    0.000 {built-in method cat}
              152184760 1586.102    0.000 1586.102    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              152184760 1391.900    0.000 1391.900    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2717585 1047.046    0.000 1388.449    0.001 replaybuffer.py:73(CF_save_data)
                2717585   44.247    0.000 1347.582    0.000 agent.py:172(__call__)
                2717585   42.621    0.000 1275.410    0.000 agent.py:112(__call__)
               13547966 1230.849    0.000 1230.849    0.000 {built-in method torch._C._nn.one_hot}
                3737748   37.364    0.000 1229.692    0.000 layers.py:849(restart)
                8152755  193.285    0.000 1206.506    0.000 optimizer.py:189(zero_grad)
             1064631020 1092.731    0.000 1092.731    0.000 layer.py:154(elements)
             4123069314  733.016    0.000 1046.428    0.000 enum.py:646(__hash__)
              271758600  158.178    0.000 1007.628    0.000 {built-in method builtins.all}
              276173606  227.198    0.000  957.199    0.000 {built-in method builtins.any}
              271331627  573.218    0.000  918.329    0.000 layers.py:246(check)
                3737748   18.958    0.000  898.150    0.000 level.py:8(__init__)
               76092380  895.034    0.000  895.034    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1885321634  480.574    0.000  881.439    0.000 layers.py:799(<genexpr>)
              271331627  500.427    0.000  836.917    0.000 layers.py:286(check)
               10830381  288.975    0.000  796.579    0.000 exploration.py:53(softmaxer)
        10960641081/10960641078  668.166    0.000  745.384    0.000 {built-in method builtins.len}
               76092380  741.745    0.000  741.745    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             2412187668  602.625    0.000  730.002    0.000 layers.py:809(<genexpr>)
               76092380  721.453    0.000  721.453    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               76092380  719.955    0.000  719.955    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3737748   77.203    0.000  690.919    0.000 levels.py:164(generate)
                2717585   53.649    0.000  666.797    0.000 replaybuffer.py:18(stacker)
                2717585   52.572    0.000  654.098    0.000 replaybuffer.py:63(stacker)
              211340536  625.176    0.000  625.176    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2717585  337.435    0.000  560.802    0.000 collector.py:46(collect)
               76092380  557.591    0.000  557.591    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7475496   70.687    0.000  512.835    0.000 level.py:41(notUsed)
              271331627  289.209    0.000  455.830    0.000 layers.py:313(check)
             5097134949  441.862    0.000  441.862    0.000 layer.py:99(positions)
              532646744  355.524    0.000  440.876    0.000 tensor.py:906(grad)
               12910666  164.693    0.000  435.419    0.000 random.py:315(sample)
              271331627  265.372    0.000  415.745    0.000 layers.py:273(check)
                8152755   11.597    0.000  397.931    0.000 loss.py:527(forward)
                8152755   30.440    0.000  386.334    0.000 functional.py:2898(mse_loss)
              271331627  234.755    0.000  353.897    0.000 layers.py:48(check)
               59630614   41.339    0.000  346.466    0.000 flatten.py:39(forward)
             4123100369  313.417    0.000  313.417    0.000 {built-in method builtins.hash}
               59630614  305.127    0.000  305.127    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               86962712  302.194    0.000  302.194    0.000 layer.py:186(<listcomp>)
               22546397  296.131    0.000  296.131    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               29901984   35.713    0.000  284.264    0.000 layer.py:77(restart)
              271331627  186.784    0.000  274.283    0.000 layers.py:23(check)
              395715743  271.252    0.000  271.252    0.000 {built-in method torch._C._get_tracing_state}
               10830381  260.066    0.000  260.066    0.000 {built-in method multinomial}
                8152755  253.846    0.000  253.846    0.000 {built-in method torch._C._nn.mse_loss}
               86962712  253.369    0.000  253.369    0.000 layer.py:187(<listcomp>)
               13549756   21.339    0.000  242.959    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624187: <Causal3_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 11 02:45:03 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 11 02:45:03 2021
Terminated at Wed May 12 02:40:38 2021
Results reported at Wed May 12 02:40:38 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   86088.32 sec.
    Max Memory :                                 3438 MB
    Average Memory :                             3404.50 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12946.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86137 sec.
    Turnaround time :                            263481 sec.

The output (if any) is above this job summary.

