
# Parameters

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH_2-0
    Main :                      Load_Cfagent
    Level :                     Levels.Coconuts
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Load name :                 Coconuts_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      57661583369 function calls (57343363228 primitive calls) in 86110.17 seconds

##    Ordered by: cumulative time
   List reduced from 434 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.174 86110.174 {built-in method builtins.exec}
                      1    4.993    4.993 86110.174 86110.174 <string>:1(<module>)
                      1  403.959  403.959 86105.180 86105.180 main.py:109(Load_Cfagent)
                8112519   36.841    0.000 21541.444    0.003 agent.py:29(learn)
                2704173 1578.813    0.001 17958.528    0.007 agent.py:212(counterfact)
                2704173   14.021    0.000 17529.155    0.006 game.py:42(step)
                8112519  550.952    0.000 17343.191    0.002 learner.py:42(Qlearn)
                2704173   18.377    0.000 16928.342    0.006 layers.py:827(step)
        353749340/35532020 1615.618    0.000 12232.089    0.000 module.py:866(_call_impl)
               27419501   82.026    0.000 11500.451    0.000 network.py:28(forward)
               27419501  359.847    0.000 11214.647    0.000 container.py:117(forward)
                2704173  273.862    0.000 11085.014    0.004 layers.py:17(step)
              269674724 1056.494    0.000 10783.819    0.000 layer.py:106(move)
                2704173  363.370    0.000 8387.605    0.003 agent.py:54(_learn)
                2704173 7107.566    0.003 8232.867    0.003 replaybuffer.py:22(sample_data)
                2704173 7023.170    0.003 8098.965    0.003 replaybuffer.py:67(sample_data)
                2704173  360.272    0.000 7660.329    0.003 agent.py:204(_learn)
               78944081 6822.028    0.000 6822.028    0.000 {built-in method tensor}
               72978999   44.292    0.000 6687.440    0.000 game.py:38(board)
                9646579  310.215    0.000 6568.426    0.001 agent.py:49(__call__)
                8112519   77.460    0.000 6562.337    0.001 optimizer.py:84(wrapper)
              269674724 1034.484    0.000 6487.080    0.000 layers.py:844(check)
                8112519   41.920    0.000 6231.661    0.001 grad_mode.py:24(decorate_context)
                8112519  284.961    0.000 6100.243    0.001 adam.py:55(step)
                4252057   84.936    0.000 6010.214    0.001 agent.py:176(choose_action)
                2704173  409.353    0.000 5796.014    0.002 layers.py:793(update)
                8112519 1265.782    0.000 5524.228    0.001 _functional.py:53(adam)
                2704173  101.188    0.000 5436.122    0.002 agent.py:117(_learn)
               75716830 3040.782    0.000 5263.212    0.000 layer.py:159(update)
                8112519   33.565    0.000 4685.788    0.001 tensor.py:195(backward)
                8112519   42.468    0.000 4651.003    0.001 __init__.py:68(backward)
                8112519 4435.222    0.001 4435.222    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               54839002  127.896    0.000 4109.456    0.000 conv.py:398(forward)
               54839002   97.892    0.000 3894.917    0.000 conv.py:390(_conv_forward)
               54839002 3797.025    0.000 3797.025    0.000 {built-in method conv2d}
                2704173 2185.160    0.001 3655.680    0.001 replaybuffer.py:28(teleporter_save_data)
                2704173 1786.153    0.001 3609.178    0.001 agent.py:88(interveen)
               76850157  159.375    0.000 3147.353    0.000 linear.py:93(forward)
               76850157   64.113    0.000 2891.862    0.000 functional.py:1737(linear)
               76850157 2812.086    0.000 2812.086    0.000 {built-in method torch._C._nn.linear}
              269674724  427.670    0.000 2514.914    0.000 layers.py:838(isFree)
                2704173 1385.605    0.001 2109.630    0.001 agent.py:67(modify)
             1793578173 1793.678    0.000 2087.244    0.000 layer.py:103(isFree)
              269674724 1395.177    0.000 1947.973    0.000 layers.py:471(check)
               39392482 1928.953    0.000 1928.953    0.000 {built-in method cat}
                2176961   33.887    0.000 1777.368    0.001 layers.py:849(restart)
              104269658  102.691    0.000 1675.325    0.000 activation.py:713(forward)
               12350752   86.312    0.000 1657.899    0.000 agent.py:59(modify_board)
              269674724 1160.479    0.000 1618.094    0.000 layers.py:77(check)
              104269658   88.249    0.000 1572.633    0.000 functional.py:1364(leaky_relu)
                2176961   15.206    0.000 1514.908    0.001 level.py:8(__init__)
              104269658 1466.618    0.000 1466.618    0.000 {built-in method torch._C._nn.leaky_relu}
              133717651 1399.982    0.000 1399.982    0.000 {built-in method clone}
                2176961   92.987    0.000 1358.827    0.001 levels.py:277(generate)
                2704173   64.535    0.000 1336.969    0.000 agent.py:172(__call__)
             4928736100  928.691    0.000 1309.304    0.000 enum.py:646(__hash__)
             1031099135 1275.042    0.000 1275.042    0.000 layer.py:154(elements)
                4252057 1067.226    0.000 1230.783    0.000 agent.py:187(convert_values)
                2704173   61.238    0.000 1206.071    0.000 agent.py:112(__call__)
               19414422  196.982    0.000 1185.824    0.000 level.py:41(notUsed)
               12350752 1086.496    0.000 1086.496    0.000 {built-in method torch._C._nn.one_hot}
              151433688 1084.950    0.000 1084.950    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              276352857  226.783    0.000  996.379    0.000 {built-in method builtins.any}
              269674724  760.808    0.000  959.867    0.000 layers.py:62(check)
                8112519  176.545    0.000  951.952    0.000 optimizer.py:189(zero_grad)
              151433688  947.469    0.000  947.469    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2704173  743.860    0.000  922.452    0.000 replaybuffer.py:73(CF_save_data)
                2704173   72.693    0.000  898.930    0.000 replaybuffer.py:18(stacker)
                2704173   72.425    0.000  862.236    0.000 replaybuffer.py:63(stacker)
              270417300   77.933    0.000  847.678    0.000 {built-in method builtins.all}
              800425791  214.545    0.000  804.743    0.000 layers.py:799(<genexpr>)
             2145922712  619.665    0.000  769.596    0.000 layers.py:809(<genexpr>)
             9655485598  625.611    0.000  697.209    0.000 {built-in method builtins.len}
             6441091629  688.143    0.000  688.143    0.000 layer.py:99(positions)
                9646579  238.896    0.000  653.969    0.000 exploration.py:53(softmaxer)
               75716844  630.863    0.000  630.863    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               19414422   16.771    0.000  567.609    0.000 level.py:38(elementsIn)
               75716844  557.519    0.000  557.519    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               75716844  510.990    0.000  510.990    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75716844  506.594    0.000  506.594    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              230108818  316.234    0.000  456.018    0.000 layers.py:113(isDone)
              530017908  366.995    0.000  451.608    0.000 tensor.py:906(grad)
                5408346  169.121    0.000  429.747    0.000 random.py:315(sample)
                2704173  253.546    0.000  427.678    0.000 collector.py:46(collect)
              317108723  302.553    0.000  421.779    0.000 layer.py:134(remove)
              269674724  272.574    0.000  407.733    0.000 layers.py:48(check)
                8112519   20.858    0.000  402.541    0.000 loss.py:527(forward)
                8112519   40.381    0.000  381.684    0.000 functional.py:2898(mse_loss)
             4928767043  380.618    0.000  380.618    0.000 {built-in method builtins.hash}
               75716844  372.045    0.000  372.045    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               19414422  182.786    0.000  369.437    0.000 level.py:39(<listcomp>)
               75716830  322.663    0.000  322.663    0.000 layer.py:171(<listcomp>)
              269674724  212.508    0.000  314.033    0.000 layers.py:23(check)
              148772576  309.697    0.000  309.697    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               54839002   48.261    0.000  277.117    0.000 flatten.py:39(forward)
              440662586  191.776    0.000  264.734    0.000 layer.py:138(add)
              894834991  250.332    0.000  250.332    0.000 level.py:32(inverse)
              290817913  245.926    0.000  245.939    0.000 module.py:934(__getattr__)
               75716830  238.524    0.000  238.524    0.000 layer.py:172(<listcomp>)
                8112519  230.840    0.000  230.840    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632955: <Coconuts_Conver4_3counterfactsNOCRASH_2_0> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:02 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 16:43:22 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 16:43:22 2021
Terminated at Thu May 13 16:38:37 2021
Results reported at Thu May 13 16:38:37 2021

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

    CPU time :                                   85904.36 sec.
    Max Memory :                                 8314 MB
    Average Memory :                             5711.50 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8070.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            89855 sec.

The output (if any) is above this job summary.

