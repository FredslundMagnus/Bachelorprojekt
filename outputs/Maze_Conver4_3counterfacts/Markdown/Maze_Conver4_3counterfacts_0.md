
# Parameters

    Name :                      Maze_Conver4_3counterfacts-0
    Main :                      CFagent
    Level :                     Levels.Maze
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


      62085993654 function calls (61711922823 primitive calls) in 86078.86 seconds

##    Ordered by: cumulative time
   List reduced from 518 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.477 86118.477 {built-in method builtins.exec}
                      1    4.389    4.389 86118.477 86118.477 <string>:1(<module>)
                      1  350.733  350.733 86114.088 86114.088 main.py:80(CFagent)
                9668976   35.915    0.000 24242.482    0.003 agent.py:29(learn)
                3222992 1724.704    0.001 21554.924    0.007 agent.py:212(counterfact)
                9668974  609.837    0.000 19747.511    0.002 learner.py:42(Qlearn)
                3222992   13.283    0.000 16012.150    0.005 game.py:42(step)
                3222992   19.952    0.000 15326.766    0.005 layers.py:827(step)
        415984873/41915733 1690.587    0.000 13785.855    0.000 module.py:866(_call_impl)
               32246759   96.040    0.000 12999.392    0.000 network.py:28(forward)
               32246759  420.518    0.000 12688.217    0.000 container.py:117(forward)
                3222992  342.427    0.000 9414.359    0.003 agent.py:54(_learn)
              103626676 9186.183    0.000 9186.183    0.000 {built-in method tensor}
               96197279   54.649    0.000 9028.423    0.000 game.py:38(board)
                3222992  289.161    0.000 8738.829    0.003 layers.py:17(step)
                3222992  339.544    0.000 8644.204    0.003 agent.py:204(_learn)
              321602024  544.081    0.000 8418.086    0.000 layer.py:106(move)
                9668974   82.401    0.000 7764.560    0.001 optimizer.py:84(wrapper)
                9668974   43.252    0.000 7394.072    0.001 grad_mode.py:24(decorate_context)
               11285374  288.823    0.000 7356.641    0.001 agent.py:49(__call__)
                9668974  299.129    0.000 7259.033    0.001 adam.py:55(step)
                4846429   94.684    0.000 6652.655    0.001 agent.py:176(choose_action)
                9668974 1505.232    0.000 6607.517    0.001 _functional.py:53(adam)
                3222993  498.089    0.000 6541.882    0.002 layers.py:793(update)
                3222992   98.391    0.000 6123.298    0.002 agent.py:117(_learn)
              103135736 3129.485    0.000 5790.127    0.000 layer.py:175(NoRock_update)
                3222992 4631.761    0.001 5638.280    0.002 replaybuffer.py:22(sample_data)
                3222992 4531.975    0.001 5499.195    0.002 replaybuffer.py:67(sample_data)
                9668974   39.108    0.000 5062.729    0.001 tensor.py:195(backward)
                9668974   38.499    0.000 5022.082    0.001 __init__.py:68(backward)
              321602024 1274.123    0.000 4860.032    0.000 layers.py:844(check)
                9668974 4791.165    0.000 4791.165    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               64493518  147.109    0.000 4680.750    0.000 conv.py:398(forward)
               64493518   92.260    0.000 4467.603    0.000 conv.py:390(_conv_forward)
               64493518 4375.342    0.000 4375.342    0.000 {built-in method conv2d}
                3222992 1652.511    0.001 3755.922    0.001 agent.py:88(interveen)
               90294293  183.406    0.000 3575.808    0.000 linear.py:93(forward)
               90294293   75.838    0.000 3299.760    0.000 functional.py:1737(linear)
                3222992 1828.375    0.001 3240.796    0.001 replaybuffer.py:28(teleporter_save_data)
               90294293 3204.709    0.000 3204.709    0.000 {built-in method torch._C._nn.linear}
              321602024  493.106    0.000 2552.418    0.000 layers.py:838(isFree)
                3222992 1579.021    0.000 2399.349    0.001 agent.py:67(modify)
                2517759   37.602    0.000 2094.182    0.001 layers.py:849(restart)
             2152716339 1742.846    0.000 2059.312    0.000 layer.py:103(isFree)
              122541052  107.439    0.000 1916.840    0.000 activation.py:713(forward)
               14508366   99.790    0.000 1899.679    0.000 agent.py:59(modify_board)
                2517759   22.954    0.000 1816.589    0.001 level.py:8(__init__)
              122541052  103.560    0.000 1809.401    0.000 functional.py:1364(leaky_relu)
               46738276 1747.160    0.000 1747.160    0.000 {built-in method cat}
              122541052 1682.182    0.000 1682.182    0.000 {built-in method torch._C._nn.leaky_relu}
                3432779  225.924    0.000 1619.301    0.000 levels.py:9(generate)
                3222990   54.418    0.000 1477.066    0.000 agent.py:172(__call__)
             1203386365 1411.924    0.000 1411.924    0.000 layer.py:154(elements)
                3222992   53.815    0.000 1406.618    0.000 agent.py:112(__call__)
              132915919 1373.038    0.000 1373.038    0.000 {built-in method clone}
              321602024  824.128    0.000 1362.118    0.000 layers.py:168(check)
                4846429 1119.864    0.000 1306.603    0.000 agent.py:187(convert_values)
              180487512 1294.112    0.000 1294.112    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              329450516  301.158    0.000 1262.933    0.000 {built-in method builtins.any}
               14508366 1228.935    0.000 1228.935    0.000 {built-in method torch._C._nn.one_hot}
              180487512 1158.037    0.000 1158.037    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9668974  207.830    0.000 1150.459    0.000 optimizer.py:189(zero_grad)
             3622402258  712.305    0.000 1019.040    0.000 enum.py:646(__hash__)
                3222992  814.616    0.000 1016.778    0.000 replaybuffer.py:73(CF_save_data)
             2878033869  781.045    0.000  961.775    0.000 layers.py:809(<genexpr>)
        12684690373/12684690370  833.506    0.000  919.199    0.000 {built-in method builtins.len}
              322299300   82.484    0.000  900.958    0.000 {built-in method builtins.all}
              834321132  225.137    0.000  866.024    0.000 layers.py:799(<genexpr>)
                3222992   55.514    0.000  758.263    0.000 replaybuffer.py:18(stacker)
               90243756  756.588    0.000  756.588    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3222990   53.501    0.000  727.471    0.000 replaybuffer.py:63(stacker)
               11285374  271.268    0.000  726.422    0.000 exploration.py:53(softmaxer)
               90243756  649.452    0.000  649.452    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               90243756  614.760    0.000  614.760    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               90243756  606.060    0.000  606.060    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              322299300  394.786    0.000  590.440    0.000 layers.py:113(isDone)
                7553277   68.724    0.000  587.979    0.000 level.py:41(notUsed)
              321602024  358.142    0.000  569.496    0.000 layers.py:141(check)
              631706376  446.719    0.000  551.893    0.000 tensor.py:906(grad)
               15829301  210.002    0.000  547.655    0.000 random.py:315(sample)
             5664694214  542.739    0.000  542.739    0.000 layer.py:99(positions)
                3222992  299.890    0.000  506.846    0.000 collector.py:46(collect)
              321602024  335.554    0.000  490.053    0.000 layers.py:48(check)
              321602024  326.221    0.000  486.162    0.000 layers.py:124(check)
                3432779  256.670    0.000  482.734    0.000 levels.py:75(RFS)
               90243756  453.157    0.000  453.157    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9668974   16.330    0.000  430.500    0.000 loss.py:527(forward)
                9668974   39.461    0.000  414.170    0.000 functional.py:2898(mse_loss)
              103135736  378.746    0.000  378.746    0.000 layer.py:186(<listcomp>)
              321602024  241.492    0.000  360.524    0.000 layers.py:23(check)
              358622029  257.099    0.000  354.170    0.000 layer.py:134(remove)
              103135736  327.848    0.000  327.848    0.000 layer.py:187(<listcomp>)
               64493518   50.753    0.000  321.304    0.000 flatten.py:39(forward)
              150647275  320.122    0.000  320.122    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             3622439025  306.742    0.000  306.742    0.000 {built-in method builtins.hash}
              499374784  209.147    0.000  301.297    0.000 layer.py:138(add)
              409479014  193.942    0.000  283.682    0.000 random.py:250(_randbelow_with_getrandbits)
               64493518  270.551    0.000  270.551    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             2898338384  258.451    0.000  258.451    0.000 {method 'random' of '_random.Random' objects}
                9668974  257.184    0.000  257.184    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9621665: <Maze_Conver4_3counterfacts_0> in cluster <dcc> Done

Job <Maze_Conver4_3counterfacts_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May  7 14:35:35 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri May  7 15:34:01 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri May  7 15:34:01 2021
Terminated at Sat May  8 15:29:28 2021
Results reported at Sat May  8 15:29:28 2021

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

    CPU time :                                   85871.77 sec.
    Max Memory :                                 9367 MB
    Average Memory :                             6313.72 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7017.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86127 sec.
    Turnaround time :                            89633 sec.

The output (if any) is above this job summary.

